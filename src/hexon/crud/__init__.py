from sqlmodel import Session, select
from sqlmodel.sql.expression import SelectOfScalar

from hexon.core.security import get_password_hash
from hexon.models import Card, CardCreate, User, UserCreate

from .crud_user import user

# For a new basic set of CRUD operations you could just do

# from .base import CRUDBase
# from app.models.item import Item
# from app.schemas.item import ItemCreate, ItemUpdate


def create_user(*, session: Session, user_create: UserCreate) -> User:
    hashed_password = get_password_hash(user_create.password)
    db_obj = User(
        email=user_create.email,
        hashed_password=hashed_password,
        is_active=user_create.is_active,
        is_superuser=user_create.is_superuser,
        full_name=user_create.full_name,
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def create_card(*, session: Session, card_create: CardCreate) -> Card:
    db_obj = Card(
        title=card_create.title,
        description=card_create.description,
        answer=card_create.answer,
        difficulty=card_create.difficulty,
        topic=card_create.topic,
    )
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_user_by_email(*, session: Session, email: str) -> User | None:
    statement: SelectOfScalar = select(User).where(User.email == email)
    session_user = session.exec(statement).first()
    return session_user
