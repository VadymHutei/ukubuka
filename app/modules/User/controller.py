from flask import request, redirect, url_for

from vendor.Ukubuka.exceptions.WrongPassword import WrongPassword
from modules.User.exceptions.UserAlreadyExist import UserAlreadyExist
from modules.User.formValidators.LoginFormValidator import LoginFormValidator
from modules.User.formValidators.RegistrationFormValidator import RegistrationFormValidator
from modules.User.service import UserService
from modules.User.views.LoginView import LoginView
from modules.User.views.RegistrationView import RegistrationView


class UserController:

    def registrationPageAction(self):
        view = RegistrationView('modules/User/registration.html')
        return view.render()

    def registrationAction(self):
        formValidator = RegistrationFormValidator(request.form)
        if formValidator.hasErrors:
            view = RegistrationView('modules/User/registration.html')
            view.addData({'errors': formValidator.errors})
            return view.render()
        service = UserService()
        try:
            service.createUser(formValidator.getFormData())
        except UserAlreadyExist as e:
            view = RegistrationView('modules/User/registration.html')
            view.addData({'errors': {'other': (str(e),)}})
            return view.render()
        return redirect(url_for('homePage', language=request.cnx['language']['code']))

    def loginPageAction(self):
        view = LoginView('modules/User/login.html')
        return view.render()

    def loginAction(self):
        formValidator = LoginFormValidator(request.form)
        if formValidator.hasErrors:
            view = LoginView('modules/User/login.html')
            view.addData({'errors': formValidator.errors})
            return view.render()
        service = UserService()
        formData = formValidator.getFormData()
        try:
            userID = service.login(formValidator.getFormData())
        except WrongPassword as e:
            view = LoginView('modules/User/login.html')
            view.addData({'errors': {'password': [e]}})
            return view.render()
        except Exception as e:
            view = LoginView('modules/User/login.html')
            view.addData({'errors': {'other': [e]}})
            return view.render()
        return redirect(url_for('homePage', language=request.cnx['language']['code']))

    def accountAction(self):
        view = AccountView('modules/User/login.html')
        return view.render()