# coding=utf-8

from typing import Optional
from sqlmodel import Field

from backend.infrastractures.postgres import BaseModel, TimeStampMixin

class UserBase(BaseModel):
    nickname: str = Field(unique=True)
    email: Optional[str]

class UserModel(UserBase, TimeStampMixin, table=True):
    __tablename__ = 'users'
    id: Optional[int] = Field(default=None, primary_key=True)

class UserRead(UserBase):
    id: int