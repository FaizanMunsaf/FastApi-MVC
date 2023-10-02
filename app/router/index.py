from fastapi import APIRouter
from app.router.api_v1 import userroute
from app.router.api_v1 import authroute
# from app.api.api_v1.handlers import todo
# from app.api.auth.jwt import auth_router

router = APIRouter()

router.include_router(authroute.auth_router, prefix='/auth', tags=["Auth"])
router.include_router(userroute.user_router, prefix='/users', tags=["Users"])