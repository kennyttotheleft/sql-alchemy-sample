# coding=utf-8

from abc import ABC, abstractmethod
from typing import Optional

from sqlmodel import select

from backend.infrastractures.postgres import RDBSession, get_db_context
from backend.models.user_model import UserModel

class UserRepository(ABC):
  @abstractmethod
  async def create(user: UserModel, db: RDBSession | None = None) -> UserModel:
    raise NotImplementedError

  @abstractmethod
  async def find_by_id(user_id: int, db: RDBSession | None = None) -> Optional[UserModel]:
    raise NotImplementedError

class RDBUserRepository(UserRepository):
  def __init__(self, db: RDBSession):
    self.db = db

  async def create(user: UserModel, db: RDBSession | None = None):
    pass

  async def find_by_id(self, id: int, db: RDBSession | None = None) -> Optional[UserModel]:
    __db = db
    if __db == None:
      __db = self.db

    statement = select(UserModel).where(UserModel.id == id)
    results = __db.exec(statement)
    return results.first()
