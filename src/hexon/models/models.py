from typing import Optional, Union

from pydantic import BaseModel
from sqlmodel import Field, SQLModel


# Shared properties
class UserBase(SQLModel):
    # email: EmailStr = Field(unique=True, index=True)
    # email: Optional[EmailStr] = Field(unique=True, index=True)
    email: str = Field(unique=True, index=True)
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    full_name: Optional[str] = Field(default=None)


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: str
    password: str
    is_active: bool
    is_superuser: bool
    full_name: Optional[str] = Field(default=None)


class UserCreateOpen(SQLModel):
    email: str
    password: str
    full_name: Union[str, None] = None


# Properties to receive via API on update, all are optional
class UserUpdate(UserBase):
    email: str
    password: Optional[str]


# Database model, database table inferred from class name
class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str


# Properties to return via API, id is always required
class UserOut(UserBase):
    id: int


# JSON payload containing access token
class Token(BaseModel):
    access_token: str
    token_type: str


# Contents of JWT token
class TokenPayload(BaseModel):
    sub: Union[int, None] = None
