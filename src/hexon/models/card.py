from typing import Optional

from sqlmodel import Field, SQLModel


# Shared properties
class CardBase(SQLModel):
    title: str
    description: str
    answer: str
    difficulty: str
    topic: str


class Card(CardBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CardCreate(CardBase):
    title: str
    description: str
    answer: str
    difficulty: str
    topic: str


# Properties to return via API, id is always required
class CardOut(CardBase):
    id: int
