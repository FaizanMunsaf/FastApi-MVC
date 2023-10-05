from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from app.model.usermodel import User
from app.schemas.userschemas import UserUpdate
from fastapi import Depends
from app.controller.usercontroller import UserController
import pymongo

from app.utils.getcurrentuser import get_current_user
from app.utils.mongodbquery import check_user
# from app.api.deps.user_deps import get_current_user


user_router = APIRouter()


@user_router.get('/getCurrentUser', summary='Get current Auth user')
async def get_current_user_by_email(user: User = Depends(get_current_user)):
    try:
        print(user)
        user_payload = {
            "email" : user.email,
            "username" : user.username
        }
        
        return JSONResponse(status_code=202,
                            content={"detail": "Current User Get Successfully", "data": user_payload, "status_code":status.HTTP_202_ACCEPTED})
    except pymongo.errors.OperationFailure:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User does not exist"
        )



