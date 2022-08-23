from datetime import datetime
from typing import Optional

from modules.User.entities.UserNameEntity import UserNameEntity


class UserEntity():

    def __init__(
        self,
        ID: Optional[int] = None,
        email: Optional[str] = None,
        name: Optional[UserNameEntity] = None,
        isBlocked: bool = False,
        registeredDatetime: Optional[datetime] = False,
    ):
        self.ID = ID
        self.email = email
        self.name = name
        self.isBlocked = isBlocked
        self.registeredDatetime = registeredDatetime