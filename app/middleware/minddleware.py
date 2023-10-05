
from fastapi import FastAPI
from app.config.config import settings


# Use for middleware 
from fastapi.middleware.cors import CORSMiddleware

# App Configrations
middleware_app = FastAPI(
title=settings.PROJECT_NAME,
openapi_url=f"{settings.API_V1_STR}openapi.json"
)

# Add middlewares
middleware_app.add_middleware(
CORSMiddleware,
allow_origins=settings.BACKEND_CORS_ORIGINS,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)