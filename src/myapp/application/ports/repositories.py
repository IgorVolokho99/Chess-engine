from typing import Protocol

from src.myapp.domain.entities.user import User


class UserRepository(Protocol):

    def add(self, user: User) -> None:
        ...

    def is_exist_user_name(self, user_name: str) -> bool:
        ...

    def save_user(self, user: User) -> None:
        ...

    def get_by_user_name(self, user_name: str) -> User:
        ...
