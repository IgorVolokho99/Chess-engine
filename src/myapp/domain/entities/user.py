import datetime


class User:
    def __init__(
            self,
            user_name: str,
            email: str,
            password_hash: str,
            id: int | None = None,
            created_at: datetime.datetime | None = None,
    ) -> None:
        self.id = id
        self.user_name = user_name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
