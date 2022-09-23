from flask import redirect, request, url_for
from modules.Base.views.View import View
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.form_validators.LoginFormValidator import LoginFormValidator
from modules.User.form_validators.RegistrationFormValidator import RegistrationFormValidator
from modules.User.services.UserService import UserService
from vendor.ukubuka.exceptions.WrongPassword import WrongPassword


class UserController:

    def registrationPageAction(self):
        view = View('modules/User/registration.html')
        return view.render()

    def registrationAction(self):
        formValidator = RegistrationFormValidator(request.form)
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
        return redirect(url_for('homeBlueprint.homeRoute', language=g.current_language.code))

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
        return redirect(url_for('homeBlueprint.homeRoute', language=g.current_language.code))

    def accountAction(self):
        view = View('modules/User/account.html')
        return view.render()
