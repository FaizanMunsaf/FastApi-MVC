from fastapi import APIRouter, HTTPException, status
from app.model.usermodel import User
from app.schemas.userschemas import UserAuth, UserOut, UserUpdate
from fastapi import Depends
from app.controller.usercontroller import UserController
import pymongo
# from app.api.deps.user_deps import get_current_user


user_router = APIRouter()


# @user_router.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
# async def get_me(user: User = Depends(get_current_user)):
#     return user


@user_router.post('/update', summary='Update User')
async def update_user(data: str):
    # try:
        return {"message":"await UserController.update_user(user.user_id, data)"}
    # except pymongo.errors.OperationFailure:
    #     raise HTTPException(
    #         status_code=status.HTTP_400_BAD_REQUEST,
    #         detail="User does not exist"
    #     )
