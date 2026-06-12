import datetime
from typing import List

from sqlalchemy import String, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.myapp.infrastructure.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, unique=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str] = mapped_column(String(30), unique=True)
    password_hash: Mapped[str] = mapped_column(String(30))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=datetime.datetime.now)

    games: Mapped[List["Game"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
    moves: Mapped[List["Move"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
    )
