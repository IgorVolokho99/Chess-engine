"""Unit-of-work service interface."""

from typing import TYPE_CHECKING, Protocol, Self

if TYPE_CHECKING:
    from types import TracebackType

    from src.myapp.application.ports.repositories import UserRepository


class UnitOfWork(Protocol):
    """Represent a domain component."""

    users: UserRepository

    def __enter__(self) -> Self:
        """Enter the managed transaction."""
        ...

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the managed transaction."""
        ...

    def commit(self) -> None:
        """Commit the current transaction."""
        ...

    def rollback(self) -> None:
        """Roll back the current transaction."""
        ...
