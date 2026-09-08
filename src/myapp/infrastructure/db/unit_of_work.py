"""Abstract database unit-of-work base class."""

from typing import TYPE_CHECKING, Self

if TYPE_CHECKING:
    from types import TracebackType


class UnitOfWork:
    """Represent a domain component."""

    def __init__(self) -> None:
        """Initialize the unit of work."""

    def __enter__(self) -> Self:
        """Enter the managed transaction."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Exit the managed transaction."""

    def commit(self) -> None:
        """Commit the current transaction."""

    def rollback(self) -> None:
        """Roll back the current transaction."""
