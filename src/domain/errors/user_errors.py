"""Содержит ошибки доменного уровня для пользовательской логики."""
from src.domain.errors.base_errors import DomainError


class UserAlreadyExistsError(DomainError):
    pass
