from typing import Protocol

from src.application.ports.repositories import UserRepository


class UnitOfWork(Protocol):
    users: UserRepository

    def __enter__(self) -> "UnitOfWork":
        ...

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        ...

    def commit(self) -> None:
        ...

    def rollback(self) -> None:
        ...