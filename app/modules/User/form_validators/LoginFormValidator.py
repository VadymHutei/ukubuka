from modules.Base.form_validators.AbstractFormValidator import AbstractFormValidator
from modules.Base.form_validators.ValidatedField import ValidatedField
from modules.User.validators.UserValidator import UserValidator


class LoginFormValidator(AbstractFormValidator):

    def _setFieldValidationRules(self):
        emailField = ValidatedField('email', required=True)
        emailField.addRule(UserValidator.email, 'Wrong email')

        passwordField = ValidatedField('password', required=True)
        passwordField.addRule(UserValidator.password, 'Wrong password')

        return (emailField, passwordField)
