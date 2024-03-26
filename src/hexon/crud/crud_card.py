from typing import Any, Dict, Optional, Union

from sqlmodel import Session, select

from hexon.crud.base import CRUDBase
from hexon.models import Card
from hexon.schemas.card import CardCreate, CardUpdate


class CRUDCard(CRUDBase[Card], CardCreate, CardUpdate):
    def create(self, db: Session, *, obj_in: Card) -> Card:
        db_obj = Card(
            title=obj_in.title,
            description=obj_in.description,
            answer=obj_in.answer,
            difficulty=obj_in.difficulty,
            topic=obj_in.topic,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    # def update(self, db: Session, *, db_obj: User, obj_in: Union[UserUpdate, Dict[str, Any]]) -> User:
    #     if isinstance(obj_in, dict):
    #         update_data = obj_in
    #     else:
    #         update_data = obj_in.model_dump(exclude_unset=True)
    #     if update_data["password"]:
    #         hashed_password = get_password_hash(update_data["password"])
    #         del update_data["password"]
    #         update_data["hashed_password"] = hashed_password
    #     return super().update(db, db_obj=db_obj, obj_in=update_data)
    #


card = CRUDCard(Card)
