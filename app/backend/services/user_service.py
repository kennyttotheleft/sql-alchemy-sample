from typing import Optional

from backend.repositories.user_repository import UserRepository
from backend.models.user_model import UserModel

class UserService:
  def __init__(self, user_repository: UserRepository):
    self.user_repository = user_repository

  async def get_user(self, user_id: int) -> UserModel:
    user: Optional[UserModel] = await self.user_repository.find_by_id(user_id)
    if not user:
      raise ValueError("User with given id does not exist")
    return user

  # TODO
  # def register_user(self, user: UserModel):
  #   existing_user = self.user_repository.find_by_id(user.id)
  #   if existing_user:
  #     raise ValueError("User with given id already exists")
  #   self.user_repository.create(user)
