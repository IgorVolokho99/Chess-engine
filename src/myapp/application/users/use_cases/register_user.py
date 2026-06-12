"""UseCase регистрации пользователя."""

from dataclasses import dataclass
from typing import Callable

from src.myapp.application.ports.password_hasher import PasswordHasher
from src.myapp.application.ports.unit_of_work import UnitOfWork
from src.myapp.domain.entities.user import User
from src.myapp.domain.errors.user_errors import UserAlreadyExistsError


@dataclass(frozen=True)
class RegisterUserCommand:
    user_name: str
    email: str
    password: str


class RegisterUserUseCase:
    def __init__(
            self,
            uow_factory: Callable[[], UnitOfWork],
            password_hasher: PasswordHasher,
    ):
        self._uow_factory = uow_factory
        self._password_hasher = password_hasher

    def execute(self, command: RegisterUserCommand) -> int:
        with self._uow_factory() as uow:
            existing_user = uow.users.get_by_user_name(command.user_name)
            if existing_user is not None:
                raise UserAlreadyExistsError("User with this user_name already exists.")

            user = User(
                user_name=command.user_name,
                email=command.email,
                password_hash=self._password_hasher.hash(command.password),
            )

            uow.users.add(user)
            uow.commit()

            if user.id is None:
                raise RuntimeError("User id was not assigned after saving")

            return user.id
