from vendor.Ukubuka.password import getPassword
from modules.User.Login.repository import LoginRepository


class LoginService:

    def __init__(self):
        self.repository = LoginRepository()

    def createUser(self, data):
        _, data['salt'], data['passwordHash'] = getPassword(password = data['password'])
        userId = self.repository.addUser(data)