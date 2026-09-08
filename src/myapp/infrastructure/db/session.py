"""Provide application functionality."""

from sqlalchemy import Engine, create_engine
from sqlalchemy.orm import sessionmaker


def build_engine(database_url: str) -> Engine:
    """Perform this operation."""
    return create_engine(
        database_url,
        echo=False,
        future=True,
    )


def build_session_factory(database_url: str) -> sessionmaker:
    """Perform this operation."""
    return sessionmaker(
        build_engine(database_url),
        autoflush=False,
        expire_on_commit=False,
    )
