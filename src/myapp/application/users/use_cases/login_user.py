from dataclasses import dataclass
from typing import Callable

from src.myapp.application.ports.password_hasher import PasswordHasher
from src.myapp.application.ports.unit_of_work import UnitOfWork
from src.myapp.domain.errors.user_errors import InvalidCredentialsError


@dataclass(frozen=True)
class LoginUserCommand:
    user_name: str
    password: str


class LoginUserUseCase:
    def __init__(
            self,
            uow_factory: Callable[[], UnitOfWork],
            password_hasher: PasswordHasher,
    ) -> None:
        self._ouw_factory = uow_factory
        self._password_hasher = password_hasher

    def execute(self, command: LoginUserCommand) -> int:
        user_name = command.user_name
        with self._ouw_factory() as uow:
            user = uow.users.get_by_user_name(user_name)

            if user is None:
                raise InvalidCredentialsError("Invalid username or password")

            is_correct_password = self._password_hasher.verify(
                raw_password=command.password,
                password_hash=user.password_hash,
            )

            if not is_correct_password:
                raise InvalidCredentialsError("Invalid username or password")

            if user.id is None:
                raise RuntimeError("User has no id.")

            return user.id
