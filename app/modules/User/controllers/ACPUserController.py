from flask import abort, g, redirect, request, url_for
from modules.User.form_validators.EditUserFormValidator import EditUserFormValidator
from modules.User.services.UserService import UserService
from modules.User.validators.UserValidator import UserValidator
from modules.User.views.EditUserACPView import EditUserACPView
from modules.User.views.UsersACPView import UsersACPView


class ACPUserController:

    def __init__(self):
        self._user_service = UserService()

    def users_page_action(self):
        view = UsersACPView()

        view.data['users'] = self._user_service.get_users()

        return view.render()

    def edit_user_page_action(self):
        user_ID = int(request.args.get('id'))
        user_entity = self._user_service.get_user_by_id(user_ID)

        if user_entity is None:
            return abort(404)

        view = EditUserACPView()

        view.data['user'] = user_entity
        view.data['form_url'] = url_for(
            endpoint='ACP_user_blueprint.ACP_edit_user_route',
            language=g.current_language.code,
            id=user_entity.ID,
        )

        return view.render()

    def edit_user_action(self):
        form_validator = EditUserFormValidator(request.form)
        form_data = form_validator.get_form_data()

        if form_validator.errors:
            try:
                return redirect(
                    location=url_for(
                        'ACP_user_blueprint.ACP_edit_user_route',
                        language=g.current_language.code,
                        id=form_data['id']
                    ),
                    code=303,
                )
            except:
                return redirect(url_for(
                    'ACP_user_blueprint.ACP_users_route',
                    language=g.current_language.code
                ))

        # self._user_service.edit_user()

        view = EditUserACPView()
        view.data['user'] = self._user_service.get_user_by_id(
            int(form_data['id']))

        return view.render()

    def block_user_action(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('ACP_user_blueprint.ACP_users_route', language=g.current_language.code))

        self._user_service.block_user(userID)

        return redirect(url_for('ACP_user_blueprint.ACP_users_route', language=g.current_language.code))

    def unblock_user_action(self):
        userID = int(request.args.get('id', 0))

        if (userID == 0 or not UserValidator.intID(userID, True)):
            return redirect(url_for('ACP_user_blueprint.ACP_users_route', language=g.current_language.code))

        self._user_service.unblock_user(userID)

        return redirect(url_for('ACP_user_blueprint.ACP_users_route', language=g.current_language.code))
