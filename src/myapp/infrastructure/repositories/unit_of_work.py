from typing import Callable

from sqlalchemy.orm import Session

from src.myapp.application.ports.repositories import UserRepository
from src.myapp.infrastructure.repositories.user_repository import SqlAlchemyUserRepository


class SqlAlchemyUnitOfWork:
    def __init__(self, session_factory: Callable[[], Session]) -> None:
        self._session_factory = session_factory
        self._session: Session | None = None
        self._committed = False

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        self._session = self._session_factory()
        self.users = SqlAlchemyUserRepository(self._session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._session is None:
            return

        try:
            if exc_type is not None or not self._committed:
                self.rollback()
        finally:
            self._session.close()

    def commit(self) -> None:
        if self._session is None:
            raise RuntimeError("UnitOfWOrk session is not initialized")

        self._session.commit()
        self._committed = True

    def rollback(self) -> None:
        if self._session is None:
            raise RuntimeError("UnitOfWOrk session is not initialized")

        self._session.rollback()
