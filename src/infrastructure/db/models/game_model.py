import datetime
from typing import List

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.domain.enums.game_result import Result
from src.domain.enums.status import Status
from src.infrastructure.db.base import Base


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))
    status: Mapped[Status]
    result: Mapped[Result]
    fen_start: Mapped[str] = Column(String(100))
    fen_current: Mapped[str] = Column(String(100))
    created_at: Mapped[datetime.datetime] = Column(DateTime, default=datetime.datetime.now)
    finished_at: Mapped[datetime.datetime] = Column(DateTime)

    user: Mapped["User"] = relationship(back_populates="games")
    moves: Mapped[List["Move"]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan",
    )
