from flask import g, redirect, request, url_for
from modules.Base.views.View import View
from modules.Notification.entities.Notification import Notification
from modules.Notification.entities.NotificationType import NotificationType
from modules.Notification.services.FormNotificationService import FormNotificationService
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.form_validators.LoginFormValidator import LoginFormValidator
from modules.User.form_validators.RegistrationFormValidator import RegistrationFormValidator
from modules.User.services.UserService import UserService
from modules.User.views.RegistrationView import RegistrationView
from vendor.ukubuka.exceptions.WrongPassword import WrongPassword


class UserController:

    _REGISTRATION_FORM_ENDPOINT = 'user_blueprint.registration_route.registration'

    def registration_page_action(self):
        view = RegistrationView()
        form_notification_service = FormNotificationService()

        view.data['errors'] = form_notification_service.pop_list(self._REGISTRATION_FORM_ENDPOINT)

        return view.render()

    def registration_action(self):
        formValidator = RegistrationFormValidator(request.form)

        if formValidator.errors:
            form_notification_service = FormNotificationService()
            for field, errors in formValidator.errors.items():
                for error in errors:
                    notification = Notification(
                        text=error,
                        type=NotificationType.ERROR_TYPE,
                        endpoint=self._REGISTRATION_FORM_ENDPOINT,
                        metadata={'field': field}
                    )
                    form_notification_service.push(notification)

            return redirect(
                location=url_for(
                    endpoint='user_blueprint.registration_route',
                    language=g.current_language.code,
                ),
                code=303,
            )

        if formValidator.errors:
            view = View('modules/User/registration.html')
            view.addData({'errors': formValidator.errors})
            return view.render()
        service = UserService()
        try:
            service.create_user(formValidator.get_form_data())
        except UserAlreadyExist as e:
            view = View('modules/User/registration.html')
            view.addData({'errors': {'other': (str(e),)}})
            return view.render()
        return redirect(url_for('home_blueprint.home_route', language=g.current_language.code))

    def loginPageAction(self):
        view = View('modules/User/login.html')
        return view.render()

    def loginAction(self):
        formValidator = LoginFormValidator(request.form)
        if formValidator.errors:
            view = View('modules/User/login.html')
            view.addData({'errors': formValidator.errors})
            return view.render()
        service = UserService()
        formData = formValidator.get_form_data()
        try:
            userID = service.login(formValidator.get_form_data())
        except WrongPassword as e:
            view = View('modules/User/login.html')
            view.addData({'errors': {'password': [e]}})
            return view.render()
        except Exception as e:
            view = View('modules/User/login.html')
            view.addData({'errors': {'other': [e]}})
            return view.render()
        return redirect(url_for('home_blueprint.home_route', language=g.current_language.code))

    def accountAction(self):
        view = View('modules/User/account.html')
        return view.render()
