"""Provide application functionality."""

from __future__ import annotations

from typing import TYPE_CHECKING, Self

from src.myapp.infrastructure.repositories.user_repository import (
    SqlAlchemyUserRepository,
)

if TYPE_CHECKING:
    from collections.abc import Callable
    from types import TracebackType

    from sqlalchemy.orm import Session


class SqlAlchemyUnitOfWork:
    """Represent a domain component."""

    def __init__(self, session_factory: Callable[[], Session]) -> None:
        """Initialize the instance."""
        self._session_factory = session_factory
        self._session: Session | None = None
        self._committed = False

    def __enter__(self) -> Self:
        """Enter the managed context."""
        self._session = self._session_factory()
        self.users = SqlAlchemyUserRepository(self._session)
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the managed context."""
        if self._session is None:
            return

        try:
            if exc_type is not None or not self._committed:
                self.rollback()
        finally:
            self._session.close()

    def commit(self) -> None:
        """Perform this operation."""
        if self._session is None:
            msg = "UnitOfWOrk session is not initialized"
            raise RuntimeError(msg)

        self._session.commit()
        self._committed = True

    def rollback(self) -> None:
        """Perform this operation."""
        if self._session is None:
            msg = "UnitOfWOrk session is not initialized"
            raise RuntimeError(msg)

        self._session.rollback()
