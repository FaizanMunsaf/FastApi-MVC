from datetime import datetime, timedelta
import time
from passlib.context import CryptContext
from typing import Optional, Union, Any, Dict
from app.config.config import settings
from jose import jwt
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.utils.auth_handler import token_response

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                print("1")
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                print("2")
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            print("3")
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeJWT(jwtoken)
            print(payload)
        except Exception as e:
            print(e)
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


# def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, settings.JWT_SECRET_KEY, settings.ALGORITHM)
#     return token_response(encoded_jwt)

def signJWT(user: dict,  expires_delta: int = None) -> Dict[str, str]:
    print(user, expires_delta)
    print(datetime.utcnow())
    if expires_delta is not None:
        expires_delta = time.time() + expires_delta
    else:
        expires_delta = time.time() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    
    payload = {
        "data": { "email": user.email, "username": user.username},
        "exp": expires_delta
    }
    print(payload)
    print(settings.JWT_SECRET_KEY)
    print(settings.ALGORITHM)
    token = jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)
    print(token)
    return token_response(token)

# def signJWT(data: dict, expires_delta: Optional[timedelta] = None):
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=10800)
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
#     return token_response(encoded_jwt)


def decodeJWT(token: str) -> dict:
    try:
        secret_key = settings.JWT_SECRET_KEY
        algo = settings.ALGORITHM
        print(type(token)," : ", token)
        print(type(settings.JWT_SECRET_KEY), " : ", secret_key)
        print(type(settings.ALGORITHM), " : ", algo)
        decoded_token = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms=[settings.ALGORITHM])
        print(decoded_token)
        return decoded_token if decoded_token["exp"] >= time.time() else None
    except Exception as e:
        # print(e)
        return {}
    
# def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
#     if expires_delta is not None:
#         expires_delta = datetime.utcnow() + expires_delta
#     else:
#         expires_delta = datetime.utcnow() + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES)
    
#     to_encode = {"exp": expires_delta, "sub": str(subject)}
#     encoded_jwt = jwt.encode(to_encode, settings.JWT_REFRESH_SECRET_KEY, settings.ALGORITHM)
#     return encoded_jwt


def get_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    print(password)
    print("3")
    return password_context.verify(password, hashed_pass)