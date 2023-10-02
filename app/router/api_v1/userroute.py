from fastapi import APIRouter, HTTPException, status
from app.schemas.userschemas import UserAuth, UserOut, UserUpdate
from fastapi import Depends
# from app.services.user_service import UserService
import pymongo
# from app.models.user_model import User
# from app.api.deps.user_deps import get_current_user


user_router = APIRouter()


# @user_router.get('/me', summary='Get details of currently logged in user', response_model=UserOut)
# async def get_me(user: User = Depends(get_current_user)):
#     return user


@user_router.post('/updateProfile', summary='Update User', response_model=UserOut)
async def update_user(data: UserUpdate):
# async def update_user(data: UserUpdate, user: User = Depends(get_current_user)):
    try:
        # return await UserService.update_user(user.user_id, data)
        return await "update"
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist"
        )
