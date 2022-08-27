from flask import abort, redirect, request, url_for
from modules.User.form_validators.EditUserFormValidator import EditUserFormValidator
from modules.User.services.UserService import UserService
from modules.User.validators.UserValidator import UserValidator
from modules.User.views.EditUserACPView import EditUserACPView
from modules.User.views.UsersACPView import UsersACPView


class ACPUserController:

    def __init__(self):
        self._userService = UserService()

    def users_page_action(self):
        view = UsersACPView()

        view.data['users'] = self._userService.get_users()

        return view.render()

    def edit_user_page_action(self):
        userID = int(request.args.get('id'))
        userEntity = self._userService.get_user_by_ID(userID)

        if userEntity is None:
            return abort(404)

        view = EditUserACPView()
        view.data['user'] = userEntity

        return view.render()

    def edit_user_action(self):
        form_validator = EditUserFormValidator()
        form_validator.validate(request.form)
        form_data = form_validator.getFormData()
        user_ID = form_data.get('id')

        if form_validator.errors:
            if user_ID is None:
                return redirect(url_for(
                    'ACP_user_Blueprint.ACP_users_route',
                    language=request.ctx['language'].code
                ))
            else:
                return redirect(url_for(
                    'ACP_user_Blueprint.ACP_edit_user_route',
                    language=request.ctx['language'].code,
                    id=user_ID
                ))

        user_entity = self._userService.get_user_by_ID(form_data['id'])

        view = EditUserACPView()
        view.data['user'] = user_entity

        return view.render()

    def block_user_action(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('ACP_user_Blueprint.ACP_users_route', language=request.ctx['language'].code))

        self._userService.block_user(userID)

        return redirect(url_for('ACP_user_Blueprint.ACP_users_route', language=request.ctx['language'].code))

    def unblock_user_action(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('ACP_user_Blueprint.ACP_users_route', language=request.ctx['language'].code))

        self._userService.unblock_user(userID)

        return redirect(url_for('ACP_user_Blueprint.ACP_users_route', language=request.ctx['language'].code))
