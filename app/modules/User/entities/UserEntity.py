from dataclasses import dataclass
from datetime import datetime

from modules.User.entities.UserNameEntity import UserNameEntity


@dataclass
class UserEntity():

    ID: int
    email: str | None
    name: UserNameEntity | None
    is_blocked: bool
    registered_datetime: datetime