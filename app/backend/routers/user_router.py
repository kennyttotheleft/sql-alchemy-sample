# coding=utf-8

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException

from backend.infrastractures.postgres import RDBSession, get_db_context
from backend.models.user_model import UserModel, UserRead
from backend.services.user_service import UserService
from backend.repositories.user_repository import UserRepository, RDBUserRepository

router = APIRouter()

@router.get("/users/{user_id}", response_model=Optional[UserRead], response_model_exclude_none=True)
async def get_user(user_id: int, db: RDBSession = Depends(get_db_context)):
    with db as __db:
        user_repository: UserRepository = RDBUserRepository(__db)
        user_service: UserService = UserService(user_repository)
        try:
            user: UserModel = await user_service.get_user(user_id)
            return user
        except ValueError as e:
            raise HTTPException(status_code=404, detail="User not found")
