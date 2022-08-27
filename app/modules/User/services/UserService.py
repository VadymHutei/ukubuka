from datetime import datetime
from typing import Union

from flask import request
from modules.Session.repository import SessionMySQLRepository
from modules.User.entities.UserEntity import UserEntity
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.exceptions.UserNotExist import UserNotExist
from modules.User.repositories.UserRepository import UserRepository
from vendor.ukubuka.exceptions.WrongPassword import WrongPassword
from vendor.ukubuka.password import getPassword


class UserService:

    def __init__(self):
        self._users_repository = UserRepository()

    def get_user_by_ID(self, user_ID: int) -> Union[UserEntity, None]:
        return self._users_repository.get_user_by_ID(user_ID)

    def create_user(self, data: dict) -> int:
        if self._users_repository.get_user_by_email(data['email']) is not None:
            raise UserAlreadyExist(f"user with same email already exist: {data['email']}")
        _, data['salt'], data['passwordHash'] = getPassword(password=data['password'])
        data['registered'] = datetime.now()
        return self._users_repository.add_user(data)

    def login(self, data: dict):
        user_data = self._users_repository.get_user_password_by_email(data['email'])
        if user_data is None:
            raise UserNotExist(f"user with this email not exist: {data['email']}")
        _, _, passwordHash = getPassword(password=data['password'], salt=user_data['salt'])
        if user_data['password_hash'] != passwordHash:
            raise WrongPassword()
        session_repository = SessionMySQLRepository()
        session_repository.setLoginStatus(request.ctx['sessionID'], user_data['id'], True)

    def logout_by_session_ID(self, session_ID: str):
        self._users_repository.logout_by_session_ID(session_ID)

    def get_users(self):
        return self._users_repository.get_users()

    def block_user(self, user_ID: int):
        self._users_repository.block_user(user_ID)

    def unblock_user(self, user_ID: int):
        self._users_repository.unblock_user(user_ID)
