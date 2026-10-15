"""Provide application functionality."""

from typing import TYPE_CHECKING

from sqlalchemy import select

from src.myapp.domain.entities.user import User
from src.myapp.infrastructure.db.models.user_model import User as UserModel

if TYPE_CHECKING:
    from sqlalchemy.orm import Session


class SqlAlchemyUserRepository:
    """Represent a domain component."""

    def __init__(self, session: Session) -> None:
        """Initialize the instance."""
        self._session = session

    def add(self, user: User) -> None:
        """Perform this operation."""
        model = UserModel(
            email=user.email,
            username=user.user_name,
            password_hash=user.password_hash,
        )
        self._session.add(model)
        self._session.flush()

        user.id = model.id
        user.created_at = model.created_at

    def get_by_user_name(self, user_name: str) -> User | None:
        """Perform this operation."""
        stmt = select(
            UserModel,
        ).where(
            UserModel.username == user_name,
        )
        model = self._session.scalar(stmt)

        if model is None:
            return None

        return User(
            entity_id=model.id,
            user_name=model.username,
            email=model.email,
            password_hash=model.password_hash,
            created_at=model.created_at,
        )

    def get_by_id(self, user_id: int) -> User | None:
        """Perform this operation."""
        model = self._session.get(UserModel, user_id)

        if model is None:
            return None

        return User(
            id=model.id,
            user_name=model.username,
            email=model.email,
            password_hash=model.password_hash,
        )
