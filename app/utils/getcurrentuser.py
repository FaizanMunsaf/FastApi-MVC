import secrets
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException

from app.infrastructure.security import JWTBearer, decodeJWT
from app.utils.mongodbquery import check_user

app = FastAPI()


# Get current user using OAuth2 authentication
async def get_current_user(token: str = Depends(JWTBearer())):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    payload = decodeJWT(token)
    if payload is None:
        raise credentials_exception
    user_payload = payload.get("data")
    email = user_payload["email"]
    if user_payload is None:
        raise credentials_exception
    user = await check_user(email)
    print(user)
    if user is None:
        raise credentials_exception
    return user

