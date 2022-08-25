from datetime import datetime

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
        self._usersRepository = UserRepository()

    def getUserByID(self, userID):
        return self._usersRepository.getUserByID(userID)

    def createUser(self, data):
        if self._usersRepository.getUserByEmail(data['email']) is not None:
            raise UserAlreadyExist(f"user with same email already exist: {data['email']}")
        _, data['salt'], data['passwordHash'] = getPassword(password = data['password'])
        data['registered'] = datetime.now()
        return self._usersRepository.addUser(data)

    def login(self, data):
        userData = self._usersRepository.getUserPasswordByEmail(data['email'])
        if userData is None:
            raise UserNotExist(f"user with this email not exist: {data['email']}")
        _, _, passwordHash = getPassword(password=data['password'], salt=userData['salt'])
        if userData['password_hash'] != passwordHash:
            raise WrongPassword()
        sessionRepository = SessionMySQLRepository()
        sessionRepository.setLoginStatus(request.ctx['sessionID'], userData['id'], True)

    def logoutBySessionID(self, sessionID):
        self._usersRepository.logoutBySessionID(sessionID)

    def getUsers(self):
        return self._usersRepository.getUsers()

    def blockUser(self, userID):
        self._usersRepository.blockUser(userID)

    def unblockUser(self, userID):
        self._usersRepository.unblockUser(userID)