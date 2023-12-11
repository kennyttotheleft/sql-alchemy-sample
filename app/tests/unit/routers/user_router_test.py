# coding=utf-8

import pytest

from backend.infrastractures.postgres import get_db_context
from backend.routers.user_router import get_user
from backend.models.user_model import UserModel
from backend.services.user_service import UserService

class TestUsersRouter:

  @pytest.mark.asyncio
  async def test_get_user(self, mocker) :

    with get_db_context() as db:
      test_user=UserModel(id=1, nickname="mike", email="mike@example.com")
      mock_get_user = mocker.patch.object(UserService, "get_user", return_value=test_user)

      user_id = 1
      user = await get_user(user_id, db)

      mock_get_user.assert_called_once_with(user_id)
      assert user.id == test_user.id
      assert user.nickname == test_user.nickname
      assert user.email == test_user.email

