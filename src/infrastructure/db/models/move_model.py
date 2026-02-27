import datetime

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, relationship

from src.infrastructure.db.base import Base


class Move(Base):
    __tablename__ = "moves"

    id: [int] = Column(Integer, unique=True, autoincrement=True, primary_key=True)
    user_id: [int] = Column(Integer, ForeignKey("user.id"))
    game_id: [int] = Column(Integer, ForeignKey("game.id"))
    move_number: [int] = Column(Integer)
    played_at: [datetime.datetime] = Column(DateTime, default=datetime.datetime.now)

    user: Mapped["User"] = relationship(back_populates="users")
    game: Mapped["Game"] = relationship(back_populates="games")
