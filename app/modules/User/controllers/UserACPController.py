from flask import request, redirect, url_for

from modules.User.form_validators.EditUserFormValidator import EditUserFormValidator
from modules.User.services.UserService import UserService
from modules.User.validators.UserValidator import UserValidator
from modules.User.views.EditUserACPView import EditUserACPView
from modules.User.views.UsersACPView import UsersACPView


class UserACPController:

    def __init__(self):
        self._userService = UserService()

    def usersPageAction(self):
        view = UsersACPView()

        view.data = {
            'users': self._userService.getUsers(),
        }

        return view.render()

    def editUserPageAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(
                url_for(
                    'userACPBlueprint.usersACPRoute',
                    language=request.ctx['language'].code
                )
            )

        user = self._userService.getUserByID(userID)

        if user is None:
            return redirect(
                url_for(
                    'userACPBlueprint.usersACPRoute',
                    language=request.ctx['language'].code
                )
            )

        view = EditUserACPView()
        view.data = {
            'user': user
        }

        return view.render()

    def editUserAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(
                url_for(
                    'userACPBlueprint.usersACPRoute',
                    language=request.ctx['language'].code
                )
            )

        view = EditUserACPView()
        user = self._userService.getUserByID(userID)

        view.data = {
            'user': user,
        }

        formValidator = EditUserFormValidator(request.form)
        if formValidator.hasErrors:
            view.error('Form errors')
            view.data = {
                'formErrors': formValidator.errors
            }

        return view.render()

    def blockUserAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(
                url_for(
                    'userACPBlueprint.usersACPRoute',
                    language=request.ctx['language'].code
                )
            )

        self._userService.blockUser(userID)

        return redirect(
            url_for(
                'userACPBlueprint.usersACPRoute',
                language=request.ctx['language'].code
            )
        )

    def unblockUserAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(
                url_for(
                    'userACPBlueprint.usersACPRoute',
                    language=request.ctx['language'].code
                )
            )

        self._userService.unblockUser(userID)

        return redirect(
            url_for(
                'userACPBlueprint.usersACPRoute',
                language=request.ctx['language'].code
            )
        )