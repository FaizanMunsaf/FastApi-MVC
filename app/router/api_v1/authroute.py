import json
from fastapi import APIRouter, Body, HTTPException, status
from app.config.config import settings
from app.infrastructure.security import signJWT
from app.schemas.userschemas import TokenSchema, UserAuth, UserLoginSchema, UserOut, UserUpdate
from fastapi import Depends
from app.controller.usercontroller import UserController
import pymongo
from fastapi.responses import JSONResponse
# from app.models.user_model import User
# from app.api.deps.user_deps import get_current_user


auth_router = APIRouter()

@auth_router.post('/signup', summary="Create new user")
async def create_user(data: UserAuth):

        data_ = await UserController.create_user(data)
        print(data_)

        if data_ == True:
            return  JSONResponse(content={"detail": "User Register Success", "data": data_, "status_code":status.HTTP_201_CREATED})
        elif data_ == False:
            return  JSONResponse(content={"detail": "User with this email already exist", "data": data_, "status_code":status.HTTP_400_BAD_REQUEST})
        
        
# @auth_router.post('/login', summary="Create new user")
# async def login_user(data: UserLoginSchema):
#      user_ = await 


@auth_router.post('/login', summary="Create access and refresh tokens for user", response_model=TokenSchema)
async def login(user: UserLoginSchema = Body(...)):
    user = await UserController.authenticate(email=user.email, password=user.password)
    print(user)
    print("4")
    sign_value = signJWT(user, settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    print(sign_value)
    
    # if not user:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="Incorrect email or password"
    #     )
    
    return sign_value