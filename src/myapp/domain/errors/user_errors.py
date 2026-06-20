"""Содержит ошибки доменного уровня для пользовательской логики."""
from src.myapp.domain.errors.base_errors import DomainError


class UserAlreadyExistsError(DomainError):
    pass


class InvalidCredentialsError(DomainError):
    pass
