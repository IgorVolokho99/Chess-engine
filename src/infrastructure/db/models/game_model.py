import datetime
from enum import Enum, auto
from typing import List

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, relationship


class Status(Enum, str):
    ACTIVE = auto
    FINISHED = auto
    ABANDONED = auto


class Result(Enum, str):
    WHITE_WIN = auto
    BLACK_WIN = auto
    DRAW = auto
    UNKNOWN = auto


class Game(DeclarativeBase):
    __tablename__ = "games"

    id: Mapped[int] = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey("user.id"))
    status: Mapped[Status]
    result: Mapped[Result]
    fen_start: Mapped[str] = Column(String(100))
    fen_current: Mapped[str] = Column(String(100))
    created_at: Mapped[datetime.datetime] = Column(DateTime, default=datetime.datetime.now)
    finished_at: Mapped[datetime.datetime] = Column(DateTime)

    user: Mapped["User"] = relationship(back_populates="users")
    moves: Mapped[List["Move"]] = relationship(back_populates="games")
