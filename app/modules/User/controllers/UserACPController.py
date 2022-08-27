from flask import abort, redirect, request, url_for
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

        view.data['users'] = self._userService.getUsers()

        return view.render()

    def editUserPageAction(self):
        userEntity = self._userService.getUserByID(int(request.args.get('id')))

        if userEntity is None:
            return abort(404)

        view = EditUserACPView()
        view.data['user'] = userEntity

        return view.render()

    def editUserAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('userACPBlueprint.usersACPRoute', language=request.ctx['language'].code))

        view = EditUserACPView()

        view.data['user'] = self._userService.getUserByID(userID)

        formValidator = EditUserFormValidator(request.form)
        if formValidator.errors:
            view.error('Form errors')
            view.data = {
                'formErrors': formValidator.errors
            }

        return view.render()

    def blockUserAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('userACPBlueprint.usersACPRoute', language=request.ctx['language'].code))

        self._userService.blockUser(userID)

        return redirect(url_for('userACPBlueprint.usersACPRoute', language=request.ctx['language'].code))

    def unblockUserAction(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('userACPBlueprint.usersACPRoute', language=request.ctx['language'].code))

        self._userService.unblockUser(userID)

        return redirect(url_for('userACPBlueprint.usersACPRoute', language=request.ctx['language'].code))
