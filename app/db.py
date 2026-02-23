from collections.abc import AsyncGenerator
import uuid
from sqlalchemy import Column, Text, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_session
from sqlalchemy.orm import DeclarativeBase, relationship
import datetime

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class Post(DeclarativeBase):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(Text, nullable = False)
    file_name = Column(Text, nullable = False)
    file_type = Column(Text, nullable = False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

