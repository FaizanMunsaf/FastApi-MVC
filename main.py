import uvicorn
import asyncio
from fastapi import FastAPI, Body, Depends

# Use for middleware 
from fastapi.middleware.cors import CORSMiddleware

# Use for Config Settings
from app.config.config import settings

# Connection Database
from app.infrastructure.dbconnection import dbConnection 

# Add Routes
from app.router.index import router


# extra test purpose
from beanie import init_beanie
from app.config.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from app.model.usermodel import User


# App Configrations
app = FastAPI(
title=settings.PROJECT_NAME,
openapi_url=f"{settings.API_V1_STR}openapi.json"
)

# Add middlewares
app.add_middleware(
CORSMiddleware,
allow_origins=settings.BACKEND_CORS_ORIGINS,
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"],
)

# Connection DataBase
@app.on_event("startup")
async def app_init():
    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).islamicgpt
    await init_beanie(
        database=db_client,
        document_models= [
            User
        ]
    )                       
       

app.include_router(router, prefix=settings.API_V1_STR)


# =============================
# For Start the uvicorn Server
async def start():
    '''Launched with 'poetry run start' at root level '''
    config = uvicorn.Config("main:app", port=8001, host='127.0.0.1',log_level="info", reload=False)
    server = uvicorn.Server(config)
    await server.serve()


# ============================
# Main Function 
if __name__ == '__main__':
    asyncio.run(start())