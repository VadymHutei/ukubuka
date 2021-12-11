from modules.User.services.UserService import UserService
from modules.User.views.UsersListACPView import UsersListACPView


class UserACPController:

    def __init__(self):
        self.userService = UserService()

    def usersListAction(self):
        view = UsersListACPView()
        users = self.userService.getUsers()

        view.data = {
            'users': users,
        }

        return view.render()