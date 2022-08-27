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
        userID = int(request.args.get('id'))
        userEntity = self._userService.getUserByID(userID)

        if userEntity is None:
            return abort(404)

        view = EditUserACPView()
        view.data['user'] = userEntity

        return view.render()

    def editUserAction(self):
        form_validator = EditUserFormValidator()
        form_validator.validate(request.form)
        form_data = form_validator.getFormData()
        user_ID = form_data.get('id')

        if form_validator.errors:
            if user_ID is None:
                return redirect(url_for(
                    'userACPBlueprint.usersACPRoute',
                    language=request.ctx['language'].code
                ))
            else:
                return redirect(url_for(
                    'userACPBlueprint.editUserACPRoute',
                    language=request.ctx['language'].code,
                    id=user_ID
                ))

        user_entity = self._userService.getUserByID(form_data['id'])

        view = EditUserACPView()
        view.data['user'] = user_entity

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
