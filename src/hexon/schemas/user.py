from typing import Optional

from pydantic import BaseModel, EmailStr
from sqlalchemy import Column, String
from sqlmodel import Field


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = Field(sa_column=Column(String))
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    email: Optional[str] = None
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        from_attributes = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
