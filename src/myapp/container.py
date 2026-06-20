# from dataclasses import dataclass
#
# from src.myapp.application.ports.unit_of_work import UnitOfWork
# from src.myapp.application.users.use_cases.register_user import RegisterUserUseCase
# from src.myapp.infrastructure import build_session_factory
#
#
#
# @dataclass(frozen=True)
# class UseCases:
#     register_user: RegisterUserUseCase
#
#
# def bootstrap(database_url: str) -> UseCases:
#     session_factory = build_session_factory(database_url)
#
#     unit_of_work = UnitOfWork(session_factory)
from dataclasses import dataclass

from sqlalchemy import Engine

from src.myapp.application.users.use_cases.login_user import LoginUserUseCase
from src.myapp.application.users.use_cases.register_user import RegisterUserUseCase
from src.myapp.infrastructure.db.session import build_session_factory
from src.myapp.infrastructure.repositories.unit_of_work import SqlAlchemyUnitOfWork
from src.myapp.infrastructure.security.werkzeud_password_hasher import WerkzeugPasswordHasher


@dataclass(frozen=True)
class UseCases:
    register_user: RegisterUserUseCase
    login_user: LoginUserUseCase


@dataclass(frozen=True)
class Container:
    # engine: Engine
    use_cases: UseCases


def bootstrap(database_url: str) -> Container:
    session_factory = build_session_factory(database_url)

    uow_factory = lambda: SqlAlchemyUnitOfWork(session_factory)
    password_hasher = WerkzeugPasswordHasher()

    user_cases = UseCases(
        register_user=RegisterUserUseCase(
            uow_factory=uow_factory,
            password_hasher=password_hasher,
        ),
        login_user=LoginUserUseCase(
            uow_factory=uow_factory,
            password_hasher=password_hasher,
        ),
    )

    return Container(
        use_cases=user_cases,
    )
