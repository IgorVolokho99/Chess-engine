import os
from pathlib import Path

from dotenv import load_dotenv


def read_secret_file(path: str) -> str:
    """Read secret from file.

    Examples:
        Local:
            secrets/db_password.txt

        Docker:
            /run/secrets/db_password

    """
    secret_path = Path(path)
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    if not secret_path.is_absolute():
        secret_path = PROJECT_ROOT / secret_path

    if not secret_path.exists():
        raise RuntimeError(f"Secret file does not exist: {secret_path}")

    value = secret_path.read_text(encoding="utf-8").strip()

    if not value:
        raise RuntimeError(f"Secret file is empty: {secret_path}")

    return value


def get_secret(
        env_name: str,
        *,
        file_env_name: str | None = None,
        default: str | None = None,
        required: bool = False,
) -> str:
    """Read secret value.

    Priority:
        1. *_FILE variable, for example DB_PASSWORD_FILE
        2. direct variable, for example DB_PASSWORD
        3. default value

    This is useful for both Docker secrets and local development.
    """
    file_env_name = file_env_name or f"{env_name}_FILE"

    secret_file = os.getenv(file_env_name)
    if secret_file:
        return read_secret_file(secret_file)

    value = os.getenv(env_name)
    if value:
        return value

    if default is not None:
        return default

    if required:
        raise RuntimeError(
            f"Secret is not configured. Set {file_env_name} or {env_name}.",
        )

    return ""


def get_database_password() -> str:
    return get_secret(
        "DB_PASSWORD",
        file_env_name="DB_PASSWORD_FILE",
        required=True,
    )


def get_database_url() -> str:
    PROJECT_ROOT = Path(__file__).resolve().parents[2]
    load_dotenv(PROJECT_ROOT / ".env.local", override=False)
    return f"{os.getenv('DB_DRIVER')}://{os.getenv('POSTGRES_USER')}:{get_database_password()}@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"


class BaseConfig:
    SECRET_KEY = "dev-secret-key"
    DATABASE_URL = get_database_url()


class DevelopmentConfig(BaseConfig):
    TESTING = True
    DATABASE_URL = get_database_url()


class ProductionConfig(BaseConfig):
    DEBUG = False
    DATABASE_URL = get_database_url()
