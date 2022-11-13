from datetime import datetime
from typing import Optional

from flask import g

from modules.Session.repositories.SessionMySQLRepository import SessionMySQLRepository
from modules.User.entities.UserEntity import UserEntity
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.exceptions.UserNotExist import UserNotExist
from modules.User.repositories.UserRepository import UserRepository


class UserService:

    def __init__(self):
        self._repository = UserRepository()

    def get_user_by_id(self, user_id: int) -> Optional[UserEntity]:
        return self._repository.get_user_by_ID(user_id)

    def get_user_by_session_id(self, session_id: str) -> Optional[UserEntity]:
        return self._repository.get_user_by_session_ID(session_id)

    def create_user(self, data: dict) -> int:
        if self._repository.get_user_by_email(data['email']) is not None:
            raise UserAlreadyExist(
                f"user with same email already exist: {data['email']}")
        _, data['salt'], data['passwordHash'] = getPassword(
            password=data['password'])
        data['registered'] = datetime.now()
        return self._repository.add_user(data)

    def login(self, data: dict):
        user_data = self._repository.get_user_password_by_email(data['email'])
        if user_data is None:
            raise UserNotExist(
                f"user with this email not exist: {data['email']}")
        _, _, passwordHash = getPassword(
            password=data['password'], salt=user_data['salt'])
        if user_data['password_hash'] != passwordHash:
            raise WrongPassword()
        session_repository = SessionMySQLRepository()
        session_repository.setLoginStatus(g.session_ID, user_data['id'], True)

    def logout_by_session_ID(self, session_ID: str):
        self._repository.logout_by_session_ID(session_ID)

    def get_users(self):
        return self._repository.get_users()

    def block_user(self, user_ID: int):
        self._repository.block_user(user_ID)

    def unblock_user(self, user_ID: int):
        self._repository.unblock_user(user_ID)
