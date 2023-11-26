from beanie import init_beanie
from fastapi import FastAPI
from app.core.config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from app.api.router import router

from app.models.userModel import User

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_STR}/openapi.json"
)

# App StartUP
@app.on_event("startup")
async def app_init():
    # initialize important application services

    db_client = AsyncIOMotorClient(settings.MONOG_CONNECTION_URI_LOCAL).interntodo

    await init_beanie(
        database=db_client,
        document_models={
            User
        }
    )

app.include_router(router, prefix=settings.API_STR)

