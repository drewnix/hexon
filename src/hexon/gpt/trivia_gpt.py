import os
import time
from typing import Optional

import openai
import requests
from openai.types.beta import Assistant

MAX_GPT_RETRIES = 100

# __location__ is used to identify the path to read prompts from
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


client = openai.OpenAI()


def download_file(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download file: HTTP {response.status_code}")


class TriviaGPT:
    def __init__(self, assistant_id: Optional[str] = None):
        self.assistant = None
        self.current_thread = None

        self.assistant = (
            self.create_assistant() if assistant_id is None else client.beta.assistants.retrieve(assistant_id)
        )

    @staticmethod
    def create_assistant() -> Assistant:
        assistant_prompt = open(os.path.join(__location__, "assistant.prompt"), "r").read()
        assistant = client.beta.assistants.create(
            name="Trivia GPT",
            instructions=assistant_prompt,
            tools=[{"type": "code_interpreter"}],
            model="gpt-4-1106-preview",
        )

        return assistant

    @staticmethod
    def initialize_thread(thread_id: Optional[str]):
        try:
            if thread_id is None:
                return client.beta.threads.create()
            else:
                return client.beta.threads.retrieve(thread_id)
        except Exception as e:
            print(f"Error initializing thread: {e}")
            raise e
            # Handle or re-raise exception as needed

    @staticmethod
    def read_and_format_prompt(count: int, topic: str):
        try:
            with open(os.path.join(__location__, "questions.prompt"), "r") as file:
                return file.read().format(count=count, topic=topic)
        except FileNotFoundError:
            print("Prompt file not found.")
            # Handle exception
        except Exception as e:
            print(f"Error reading prompt file: {e}")
            raise e
            # Handle exception

    def get_questions(
        self, count: Optional[int] = 20, topic: Optional[str] = "hodgepodge", thread_id: Optional[str] = None
    ):
        self.current_thread = self.initialize_thread(thread_id)
        rendered_prompt = self.read_and_format_prompt(count, topic)

        message = client.beta.threads.messages.create(
            thread_id=self.current_thread.id, role="user", content=rendered_prompt
        )

        run = client.beta.threads.runs.create(
            thread_id=self.current_thread.id,
            assistant_id=self.assistant.id,
        )

        for i in range(MAX_GPT_RETRIES):
            time.sleep(5)
            run_status = client.beta.threads.runs.retrieve(
                thread_id=self.current_thread.id,
                run_id=run.id,
            )
            print(f"Waiting for chatgpt run completion... iteration #{i}, current_status: {run_status.status}")
            if run_status.status == "completed":
                messages = client.beta.threads.messages.list(thread_id=self.current_thread.id)
                raw_json = messages.data[0].content[0].text.value
                import pdb

                pdb.set_trace()
                return raw_json

        print("Run did not complete in time.")
        raise Exception(f"ChatGPT run did not complete in time")


if __name__ == "__main__":
    trivia_gpt = TriviaGPT()
    raw = trivia_gpt.get_questions(20, "hodgepodge")
    with open("trivia_gpt.json", "w") as fh:
        fh.write(raw)
