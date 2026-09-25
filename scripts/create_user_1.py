"""Create the local development user with username and password ``1``.

Run after applying migrations:

    uv run python scripts/create_user_1.py

or:

    uv run python -m scripts.create_user_1
"""

# ruff: noqa: I001 -- direct execution must set sys.path before project imports.

import sys
from pathlib import Path

from sqlalchemy import select

# Running this file directly makes Python put ``scripts/`` on sys.path, rather
# than the repository root where the ``src`` package lives.
if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.myapp.infrastructure.config import get_database_url
from src.myapp.infrastructure.db.models.user_model import User
from src.myapp.infrastructure.db.session import build_session_factory
from src.myapp.infrastructure.security.werkzeud_password_hasher import (
    WerkzeugPasswordHasher,
)


USERNAME = "1"
PASSWORD = "1"  # noqa: S105 -- intentional local development credential
EMAIL = "user1@example.com"


def main() -> None:
    """Create the development account or reset its password."""
    session = build_session_factory(get_database_url())()
    password_hash = WerkzeugPasswordHasher().hash(PASSWORD)
    try:
        user = session.scalar(select(User).where(User.username == USERNAME))
        if user is None:
            session.add(
                User(
                    username=USERNAME,
                    email=EMAIL,
                    password_hash=password_hash,
                ),
            )
            action = "Created"
        else:
            user.password_hash = password_hash
            action = "Reset password for"

        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

    print(f"{action} user '{USERNAME}'.")  # noqa: T201


if __name__ == "__main__":
    main()
