"""Provide application functionality."""

from typing import TYPE_CHECKING

from src.myapp.domain.errors.user_errors import UserNotFoundError

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.myapp.application.ports.unit_of_work import UnitOfWork
    from src.myapp.domain.entities.user import User


class GetCurrentUserUseCase:
    """Represent a domain component."""

    def __init__(
        self,
        uow_factory: Callable[[], UnitOfWork],
    ) -> None:
        """Initialize the instance."""
        self._ouw_factory = uow_factory

    def execute(self, user_id: int) -> User:
        """Perform this operation."""
        with self._ouw_factory() as uow:
            user = uow.users.get_by_id(user_id)

            if user is None or user.id is None:
                raise UserNotFoundError

            return user
