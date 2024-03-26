import random
from typing import Dict, List, Optional

from fastapi import APIRouter, Depends
from sqlmodel import select, or_
from sqlmodel.sql.expression import SelectOfScalar

from hexon import crud
from hexon.api.deps import SessionDep, get_current_active_superuser
from hexon.models.card import Card, CardCreate, CardOut

router = APIRouter()


@router.get("/")
async def read_cards(session: SessionDep, topic: Optional[str] = None) -> Dict[str, str]:
    # Here you'll add logic to select a flashcard based on the topic
    # For demonstration, I'll return a hardcoded flashcard
    if topic:
        statement = select(Card).where(Card.topic == topic)
    else:
        statement = select(Card)
    cards = session.exec(statement).all()

    if not cards:
        return {"message": "No cards found for the specified topic."}

    card = random.choice(cards)
    return {"title": card.title, "description": card.description, "topic": card.topic, "answer": card.answer}


@router.post("/", dependencies=[Depends(get_current_active_superuser)])
def create_card(*, session: SessionDep, card_in: CardCreate) -> CardOut:
    # TODO: add existing card check
    card = crud.create_card(session=session, card_create=card_in)
    return card  # type: ignore


@router.get("/topics", response_model=List[str])
async def read_distinct_topics(session: SessionDep) -> List[str]:
    # Use SQLModel's select function to query distinct topics
    statement = select(Card.topic).distinct()
    results = session.exec(statement)
    topics = results.all()
    return topics