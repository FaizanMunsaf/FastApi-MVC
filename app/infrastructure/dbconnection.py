
from beanie import init_beanie
from app.config.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from app.model.usermodel import User


# class mongoConnection:
    # async def __init__(self):
        
    #     # self.db_client = AsyncIOMotorClient("mongodb://localhost:27017").islamicgpt
        
        
        
async def dbConnection():
    """
    initialize crucial application services
    """

    db_client = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).islamicgpt
    await init_beanie(
        database=db_client,
        document_models= [
            User
        ]
    )                       
        

# connection = mongoConnection()
