import json

from sqlmodel import Session, SQLModel, select

from hexon import crud
from hexon.core.config import settings
from hexon.db.engine import engine
from hexon.models import Card, User, UserCreate  # noqa: F401

# make sure all SQLModel models are imported (app.models) before initializing DB
# otherwise, SQLModel might fail to initialize relationships properly


def init_db(session: Session) -> None:
    # Tables should be created with Alembic migrations
    # But if you don't want to use migrations, create
    # the tables un-commenting the next line
    SQLModel.metadata.create_all(bind=engine)
    user = session.exec(select(User).where(User.email == settings.FIRST_SUPERUSER)).first()
    if not user:
        user_in = UserCreate(
            email=settings.FIRST_SUPERUSER,
            password=settings.FIRST_SUPERUSER_PASSWORD,
            full_name="superuser",
            is_active=True,
            is_superuser=True,
        )
        user = crud.create_user(session=session, user_create=user_in)


def load_cards(session: Session) -> None:
    raw_json = open("metadata/cards.json", "r").read()
    cards = json.loads(raw_json)
    for card in cards:
        db_obj = Card(
            title=card["title"],
            description=card["description"],
            answer=card["answer"],
            difficulty=card["difficulty"],
            topic=card["topic"],
        )
        session.add(db_obj)

    session.commit()
