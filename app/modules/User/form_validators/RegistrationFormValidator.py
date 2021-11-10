from vendor.ukubuka.AbstractFormValidator import AbstractFormValidator
from vendor.ukubuka.ValidatedField import ValidatedField
from modules.User.validator import UserValidator


class RegistrationFormValidator(AbstractFormValidator):

    def setRules(self):
        emailField = ValidatedField('email', required = True)
        emailField.addRule(
            UserValidator.email,
            'Wrong email'
        )

        passwordField = ValidatedField('password', required = True)
        passwordField.addRule(
            UserValidator.password,
            'Wrong password'
        )
        return (emailField, passwordField)