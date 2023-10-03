from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field


class UserAuth(BaseModel):
    email: EmailStr = Field(..., description="user email")
    username: str = Field(..., min_length=5, max_length=50, description="user username")
    password: str = Field(..., min_length=5, max_length=24, description="user password")
    

class UserOut(BaseModel):
    user_id: UUID
    username: str
    email: EmailStr
    phone_number: Optional[str]
    user_image: Optional[str]
    # disabled: Optional[bool] = False
    

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., min_length=5, max_length=24, description="user password")

class TokenSchema(BaseModel):
    access_token: str