from fastapi import FastAPI, HTTPException
from app.schemas import CreatePost, PostResponse
from app.db import Post, create_database, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield

app = FastAPI(lifespan=lifespan)
