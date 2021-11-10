from datetime import datetime

from flask import request

from vendor.ukubuka.exceptions.WrongPassword import WrongPassword
from vendor.ukubuka.password import getPassword
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.exceptions.UserNotExist import UserNotExist
from modules.User.repository import UserRepository
from modules.Session.repository import SessionMySQLRepository


class UserService:

    def __init__(self):
        self.repository = UserRepository()

    def getUserByID(self, userID):
        data = self.repository.getUserByID(userID)
        return User(data) if data else None

    def createUser(self, data):
        if self.repository.getUserByEmail(data['email']) is not None:
            raise UserAlreadyExist(f"user with same email already exist: {data['email']}")
        _, data['salt'], data['passwordHash'] = getPassword(password = data['password'])
        data['registered'] = datetime.now()
        return self.repository.addUser(data)

    def login(self, data):
        userData = self.repository.getUserPasswordByEmail(data['email'])
        if userData is None:
            raise UserNotExist(f"user with this email not exist: {data['email']}")
        _, _, passwordHash = getPassword(password=data['password'], salt=userData['salt'])
        if userData['password_hash'] != passwordHash:
            raise WrongPassword()
        sessionRepository = SessionMySQLRepository()
        sessionRepository.setLoginStatus(request.ctx['sessionID'], userData['id'], True)

    def logoutBySessionID(self, sessionID):
        self.repository.logoutBySessionID(sessionID)