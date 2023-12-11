# coding=utf-8

import pytest
from sqlalchemy import text

from backend.infrastractures.postgres import get_db_context
from backend.models.user_model import UserModel
from backend.services.user_service import UserService
from backend.repositories.user_repository import UserRepository, RDBUserRepository

class TestUserRepository:
  @classmethod
  def setup_class(cls):
    db_context = get_db_context()
    with db_context as db:
      db.execute(text("TRUNCATE TABLE users"))
      db.commit()
      db.close()

  @classmethod
  def teardown_class(cls):
    pass

  @pytest.mark.asyncio
  async def test_find_by_id(self, mocker) :
    db_context = get_db_context()
    with db_context as db:
      test_user = UserModel(nickname="test-nickname", email='test@example.com')
      db.add(test_user)
      db.commit()

      user_id = test_user.id
      user_repo = RDBUserRepository(db)
      user = await user_repo.find_by_id(user_id, db)

      assert user.id == test_user.id
      assert user.nickname == test_user.nickname
      assert user.email == test_user.email

      db.delete(test_user)
      db.commit()
