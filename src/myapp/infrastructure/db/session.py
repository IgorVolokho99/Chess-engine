from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker


def build_engine(database_url) -> Engine:
    return create_engine(
        database_url,
        echo=False,
        future=True,
    )


def build_session_factory(database_url: str) -> sessionmaker:
    return sessionmaker(
        build_engine(database_url),
        autoflush=False,
        expire_on_commit=False,
    )
