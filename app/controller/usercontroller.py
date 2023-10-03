from typing import Optional
from uuid import UUID
from app.schemas.userschemas import UserAuth, UserLoginSchema
from app.model.usermodel import User
from app.infrastructure.security import get_password, verify_password
import pymongo


class UserController:
    @staticmethod
    async def create_user(user: UserAuth):
        try:
            user_in = User(
                username=user.username,
                email=user.email,
                hashed_password=get_password(user.password)
            )
            await user_in.save()
            return True
        except:
            return False
        
    
    @staticmethod
    async def authenticate(email: str, password: str) -> Optional[User]:
        user = await UserController.get_user_by_email(email=email)
        print(user)
        print("2")
        if not user:
            return None
        if not verify_password(password=password, hashed_pass=user.hashed_password):
            return None
        
        return user
        
    @staticmethod
    async def get_user_by_email(email: str) -> Optional[User]:
        print(email)
        user = await User.find_one(User.email == email)
        print("1 : ", user)
        # print(user)
        return user