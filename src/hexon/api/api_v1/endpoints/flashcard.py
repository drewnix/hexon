from typing import Dict
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_flashcard(topic: str) -> Dict[str, str]:
    # Here you'll add logic to select a flashcard based on the topic
    # For demonstration, I'll return a hardcoded flashcard
    flashcard = {
        "title": "Sample Flashcard",
        "subtitle": "Subtitle based on topic: " + topic,
        "description": "What is the capital of France?",
        "answer": "Paris"
    }
    return flashcard
