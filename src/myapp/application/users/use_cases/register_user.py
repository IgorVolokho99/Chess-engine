"""UseCase регистрации пользователя."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

from src.myapp.domain.entities.user import User
from src.myapp.domain.errors.user_errors import UserAlreadyExistsError

if TYPE_CHECKING:
    from collections.abc import Callable

    from src.myapp.application.ports.password_hasher import PasswordHasher
    from src.myapp.application.ports.unit_of_work import UnitOfWork


@dataclass(frozen=True)
class RegisterUserCommand:
    """Represent a domain component."""

    user_name: str
    email: str
    password: str


class RegisterUserUseCase:
    """Represent a domain component."""

    def __init__(
        self,
        uow_factory: Callable[[], UnitOfWork],
        password_hasher: PasswordHasher,
    ) -> None:
        """Initialize the instance."""
        self._uow_factory = uow_factory
        self._password_hasher = password_hasher

    def execute(self, command: RegisterUserCommand) -> int:
        """Perform this operation."""
        with self._uow_factory() as uow:
            existing_user = uow.users.get_by_user_name(command.user_name)
            if existing_user is not None:
                msg = "User with this user_name already exists."
                raise UserAlreadyExistsError(msg)

            user = User(
                user_name=command.user_name,
                email=command.email,
                password_hash=self._password_hasher.hash(command.password),
            )

            uow.users.add(user)
            uow.commit()

            if user.id is None:
                msg = "User id was not assigned after saving"
                raise RuntimeError(msg)

            return user.id
