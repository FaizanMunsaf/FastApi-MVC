from fastapi import APIRouter, HTTPException, status
from app.schemas.userschemas import UserAuth, UserOut, UserUpdate
from fastapi import Depends
from app.controller.usercontroller import UserController
import pymongo
# from app.models.user_model import User
# from app.api.deps.user_deps import get_current_user


auth_router = APIRouter()

@auth_router.post('/signup', summary="Create new user", response_model=UserOut)
async def create_user(data: UserAuth):
    try:
        return await UserController.create_user(data)
    # except pymongo.errors.DuplicateKeyError:
    except:
        print("*******************")
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email or username already exist"
        )
        

