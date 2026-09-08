"""Provide application functionality."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.myapp.domain.errors.user_errors import InvalidCredentialsError

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.myapp.application.ports.password_hasher import PasswordHasher
    from src.myapp.application.ports.unit_of_work import UnitOfWork


@dataclass(frozen=True)
class LoginUserCommand:
    """Represent a domain component."""

    user_name: str
    password: str


class LoginUserUseCase:
    """Represent a domain component."""

    def __init__(
        self,
        uow_factory: Callable[[], UnitOfWork],
        password_hasher: PasswordHasher,
    ) -> None:
        """Initialize the instance."""
        self._ouw_factory = uow_factory
        self._password_hasher = password_hasher

    def execute(self, command: LoginUserCommand) -> int:
        """Perform this operation."""
        user_name = command.user_name
        with self._ouw_factory() as uow:
            user = uow.users.get_by_user_name(user_name)

            if user is None:
                msg = "Invalid username or password"
                raise InvalidCredentialsError(msg)

            is_correct_password = self._password_hasher.verify(
                raw_password=command.password,
                password_hash=user.password_hash,
            )

            if not is_correct_password:
                msg = "Invalid username or password"
                raise InvalidCredentialsError(msg)

            if user.id is None:
                msg = "User has no id."
                raise RuntimeError(msg)

            return user.id
