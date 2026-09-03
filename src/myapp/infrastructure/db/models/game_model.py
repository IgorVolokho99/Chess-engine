import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from src.myapp.domain.enums.game_result import GameResult
from src.myapp.domain.enums.status import GameStatus
from src.myapp.infrastructure.db.base import Base

if TYPE_CHECKING:
    from src.myapp.infrastructure.db import Move, User


class Game(Base):
    __tablename__ = "games"

    id: Mapped[int] = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    user_id: Mapped[int] = Column(Integer, ForeignKey("users.id"))
    status: Mapped[GameStatus]
    result: Mapped[GameResult]
    fen_start: Mapped[str] = Column(String(100))
    fen_current: Mapped[str] = Column(String(100))
    created_at: Mapped[datetime.datetime] = Column(DateTime, default=datetime.datetime.now)
    finished_at: Mapped[datetime.datetime] = Column(DateTime)

    user: Mapped[User] = relationship(back_populates="games")
    moves: Mapped[list[Move]] = relationship(
        back_populates="game",
        cascade="all, delete-orphan",
    )
