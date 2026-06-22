from dataclasses import dataclass

from src.myapp.application.users.use_cases.get_current_user import GetCurrentUserUseCase
from src.myapp.application.users.use_cases.login_user import LoginUserUseCase
from src.myapp.application.users.use_cases.register_user import RegisterUserUseCase
from src.myapp.infrastructure.db.session import build_session_factory
from src.myapp.infrastructure.repositories.unit_of_work import SqlAlchemyUnitOfWork
from src.myapp.infrastructure.security.werkzeud_password_hasher import WerkzeugPasswordHasher


@dataclass(frozen=True)
class UseCases:
    register_user: RegisterUserUseCase
    login_user: LoginUserUseCase
    get_current_user: GetCurrentUserUseCase


@dataclass(frozen=True)
class Container:
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
        get_current_user=GetCurrentUserUseCase(
            uow_factory=uow_factory,
        ),
    )

    return Container(
        use_cases=user_cases,
    )
