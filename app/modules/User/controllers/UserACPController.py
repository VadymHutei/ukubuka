from modules.User.services.UserService import UserService
from modules.User.views.UsersACPView import UsersACPView


class UserACPController:

    def __init__(self):
        self.userService = UserService()

    def usersAction(self):
        view = UsersACPView()
        users = self.userService.getUsers()

        view.data = {
            'users': users,
        }

        return view.render()