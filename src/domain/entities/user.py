import datetime


class User:
    def __init__(
            self,
            id: int,
            name: str,
            email: str,
            password_hash: str,
            created_at: datetime.datetime,
    ) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.created_at = created_at
