# coding=utf-8

import pytest

from backend.infrastractures.postgres import get_db_context
from backend.models.user_model import UserModel
from backend.services.user_service import UserService
from backend.repositories.user_repository import UserRepository, RDBUserRepository

class TestUserService:

  @pytest.mark.asyncio
  async def test_get_user(self, mocker) :
    db_context = get_db_context()
    with db_context as db:
      test_user = UserModel(id=1, nickname="mike", email="mike@example.com")
      mock_user_repo: UserRepository = RDBUserRepository(db)
      mock_find_by_id = mocker.patch.object(mock_user_repo, "find_by_id", return_value=test_user)

      user_service = UserService(user_repository=mock_user_repo)
      user_id = 1
      user = await user_service.get_user(user_id)

      mock_find_by_id.assert_called_once()
      mock_find_by_id.assert_called_once_with(user_id)
      assert mock_find_by_id.call_args_list[0][0][0] == user_id
      assert user.id == test_user.id
      assert user.nickname == test_user.nickname
      assert user.email == test_user.email

