from abc import ABC, abstractmethod

from src.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    def is_exist_user_name(self, user_name: str) -> bool:
        ...

    @abstractmethod
    def save_user(self, user: User) -> None:
        ...
