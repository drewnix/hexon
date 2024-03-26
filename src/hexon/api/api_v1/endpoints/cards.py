import random
from typing import Dict

from fastapi import APIRouter, Depends
from sqlmodel import select
from sqlmodel.sql.expression import SelectOfScalar

from hexon import crud
from hexon.api.deps import SessionDep, get_current_active_superuser
from hexon.models.card import Card, CardCreate, CardOut

router = APIRouter()


@router.get("/")
async def read_cards(session: SessionDep, topic: str) -> Dict[str, str]:
    # Here you'll add logic to select a flashcard based on the topic
    # For demonstration, I'll return a hardcoded flashcard
    statement: SelectOfScalar = select(Card)
    cards = session.exec(statement).all()
    card = random.choice(cards)
    c = {"title": card.title, "description": card.description, "topic": card.topic, "answer": card.answer}
    return c


@router.post("/", dependencies=[Depends(get_current_active_superuser)])
def create_card(*, session: SessionDep, card_in: CardCreate) -> CardOut:
    # TODO: add existing card check
    card = crud.create_card(session=session, card_create=card_in)
    return card  # type: ignore
