from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import uvicorn
import asyncio
from fastapi import FastAPI, Body, Depends
# from app.infrastructure.exception import exception_app
from app.infrastructure.exception import validation_exception_handler

from app.middleware.minddleware import middleware_app
# from app.infrastructure.exception import exception_app

# Use for Config Settings
from app.config.config import settings

# Connection Database
from app.infrastructure.dbconnection import dbConnection

# Add Routes
from app.router.index import router


# App Configrations
app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}openapi.json"
)

# add middleware
app.mount("/middleware_app", middleware_app)
# app.mount("/exception_app",exception_app)

# Exception Handler Call for email


@app.exception_handler(RequestValidationError)
async def custom_validation_exception_handler(request, exc):
    return await validation_exception_handler(request, exc)


# Connection DataBase
@app.on_event("startup")
async def app_init():
    await dbConnection()

# Inculde the routers
app.include_router(router, prefix=settings.API_V1_STR)


# =============================
# For Start the uvicorn Server
def start():
    '''Launched with 'poetry run start' at root level '''
    uvicorn.run("main:app", port=8001, host='127.0.0.1',
                log_level="info", reload=True)
    # config = uvicorn.Config("main:app", port=8001, host='127.0.0.1',log_level="info", reload=True)
    # server = uvicorn.Server(config)
    # await server.serve()


# ============================
# Main Function
if __name__ == '__main__':
    # asyncio.run(start())
    start()
