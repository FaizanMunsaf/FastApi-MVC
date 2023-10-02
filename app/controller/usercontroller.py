from typing import Optional
from uuid import UUID
from app.schemas.userschemas import UserAuth
from app.model.usermodel import User
from app.infrastructure.security import get_password, verify_password
import pymongo


class UserController:
    @staticmethod
    async def create_user(user: UserAuth):
        user_in = User(
            username=user.username,
            email=user.email,
            hashed_password=get_password(user.password)
        )
        await user_in.save()
        return user_in