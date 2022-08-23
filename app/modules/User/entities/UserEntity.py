from typing import Optional

from modules.User.entities.UserNameEntity import UserNameEntity


class UserEntity():

    def __init__(
        self,
        ID: Optional[int] = None,
        email: Optional[str] = None,
        name: Optional[UserNameEntity] = None,
    ):
        self.ID = int(ID)
        self.email = email
        self.name = name