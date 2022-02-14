from modules.User.validators.UserValidator import UserValidator
from vendor.ukubuka.AbstractFormValidator import AbstractFormValidator
from vendor.ukubuka.ValidatedField import ValidatedField


class EditUserFormValidator(AbstractFormValidator):

    def setRules(self):
        emailField = ValidatedField('email', required=False)
        emailField.addRule(
            UserValidator.email,
            'Wrong email'
        )

        passwordField = ValidatedField('password', required=False)
        passwordField.addRule(
            UserValidator.password,
            'Wrong password'
        )

        firstNameField = ValidatedField('first_name', required=False, emptyAllowed=True)
        firstNameField.addRule(
            UserValidator.name,
            'Wrong first name'
        )

        lastNameField = ValidatedField('last_name', required=False, emptyAllowed=True)
        lastNameField.addRule(
            UserValidator.name,
            'Wrong last name'
        )

        return (emailField, passwordField, firstNameField, lastNameField)