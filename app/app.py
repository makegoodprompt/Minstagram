from fastapi import FastAPI, HTTPException, File, UploadFile, Form, Depends
from app.schemas import CreatePost, PostResponse
from app.db import Post, create_database, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_database()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/uplaod")
async def upload(
        file: UploadFile = File(...),
        caption: str = Form(""),
        session: AsyncSession = Depends(get_async_session)
):
    post = Post(
        caption=caption,
        url="some url",
        file_type="Photo",
        file_name="some file name",
    )
    session.add(post)
    await session.commit()
    await session.refresh(post)
    return post