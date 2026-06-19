import datetime
from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.myapp.infrastructure.db.base import Base

if TYPE_CHECKING:
    from src.myapp.infrastructure.db import User, Game

class Move(Base):
    __tablename__ = "moves"

    id: [int] = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    user_id: [int] = Column(Integer, ForeignKey("users.id"))
    game_id: [int] = Column(Integer, ForeignKey("games.id"))
    move_number: [int] = Column(Integer)
    played_at: [datetime.datetime] = Column(DateTime, default=datetime.datetime.now)

    user: Mapped["User"] = relationship(back_populates="moves")
    game: Mapped["Game"] = relationship(back_populates="moves")
