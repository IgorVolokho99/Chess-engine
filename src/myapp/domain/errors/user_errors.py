"""Содержит ошибки доменного уровня для пользовательской логики."""

from src.myapp.domain.errors.base_errors import DomainError


class UserAlreadyExistsError(DomainError):
    """Represent a domain component."""


class InvalidCredentialsError(DomainError):
    """Represent a domain component."""


class UserNotFoundError(DomainError):
    """Represent a domain component."""
