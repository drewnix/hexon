import { ModeToggle } from "@/components/mode-toggle.tsx";
import FlashCard from "@/components/flashcard.tsx";
import {TopicSelect} from "@/components/topic-select.tsx";

function Hexon() {
    return (
        <div className="bg-background flex flex-col justify-center items-center pt-20">
            <div className="w-full border-2 max-w-3xl mb-8 mx-auto p-6 bg-card rounded-md shadow relative">
                <div className="flex justify-between items-start">
                    <h1 className="scroll-m-20 text-4xl font-extrabold tracking-tight lg:text-5xl">
                        Trivia GPT
                    </h1>
                    <ModeToggle/>
                </div>
                <p className="leading-7 pl-1 [&:not(:first-child)]:mt-6">
                    Select an existing topic or have Trivia GPT create one.
                </p>
                <br/>
                <TopicSelect/>

            </div>

            <FlashCard/>
        </div>
    )
}

export default Hexon;
