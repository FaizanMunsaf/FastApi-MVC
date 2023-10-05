from typing import Optional
from app.model.usermodel import User
from app.schemas.userschemas import UserLoginSchema


async def check_user(email: str) -> Optional[User]:
    print(email)
    user = await User.find_one(User.email == email)
    print(user)
    return user
