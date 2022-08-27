from flask import redirect, request, url_for
from modules.Ukubuka.views.UkubukaView import UkubukaView
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.form_validators.LoginFormValidator import LoginFormValidator
from modules.User.form_validators.RegistrationFormValidator import RegistrationFormValidator
from modules.User.services.UserService import UserService
from vendor.ukubuka.exceptions.WrongPassword import WrongPassword


class UserController:

    def registrationPageAction(self):
        view = UkubukaView('modules/User/registration.html')
        return view.render()

    def registrationAction(self):
        formValidator = RegistrationFormValidator(request.form)
        if formValidator.errors:
            view = UkubukaView('modules/User/registration.html')
            view.addData({'errors': formValidator.errors})
            return view.render()
        service = UserService()
        try:
            service.create_user(formValidator.getFormData())
        except UserAlreadyExist as e:
            view = UkubukaView('modules/User/registration.html')
            view.addData({'errors': {'other': (str(e),)}})
            return view.render()
        return redirect(url_for('homeBlueprint.homeRoute', language=request.ctx['language'].code))

    def loginPageAction(self):
        view = UkubukaView('modules/User/login.html')
        return view.render()

    def loginAction(self):
        formValidator = LoginFormValidator(request.form)
        if formValidator.errors:
            view = UkubukaView('modules/User/login.html')
            view.addData({'errors': formValidator.errors})
            return view.render()
        service = UserService()
        formData = formValidator.getFormData()
        try:
            userID = service.login(formValidator.getFormData())
        except WrongPassword as e:
            view = UkubukaView('modules/User/login.html')
            view.addData({'errors': {'password': [e]}})
            return view.render()
        except Exception as e:
            view = UkubukaView('modules/User/login.html')
            view.addData({'errors': {'other': [e]}})
            return view.render()
        return redirect(url_for('homeBlueprint.homeRoute', language=request.ctx['language'].code))

    def accountAction(self):
        view = UkubukaView('modules/User/account.html')
        return view.render()
