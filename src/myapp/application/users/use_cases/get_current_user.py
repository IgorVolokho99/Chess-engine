from typing import Callable

from src.myapp.application.ports.unit_of_work import UnitOfWork
from src.myapp.domain.entities.user import User
from src.myapp.domain.errors.user_errors import UserNotFoundError


class GetCurrentUserUseCase:
    def __init__(
        self,
        uow_factory: Callable[[], UnitOfWork]
    ) -> None:
        self._ouw_factory = uow_factory

    def execute(self, user_id: int) -> User:
        with self._ouw_factory() as uow:
            user = uow.users.get_by_id(user_id)

            if user is None or user.id is None:
                raise UserNotFoundError()

            return user
