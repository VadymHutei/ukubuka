from datetime import datetime
from typing import Optional

from modules.User.entities.UserNameEntity import UserNameEntity


class UserEntity():

    def __init__(
        self,
        ID: int,
        email: Optional[str],
        name: Optional[UserNameEntity],
        is_blocked: bool,
        registered_datetime: datetime,
    ):
        self.ID = ID
        self.email = email
        self.name = name
        self.is_blocked = is_blocked
        self.registered_datetime = registered_datetime
