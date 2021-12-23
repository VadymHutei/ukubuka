from modules.User.validators.UserValidator import UserValidator
from vendor.ukubuka.AbstractFormValidator import AbstractFormValidator
from vendor.ukubuka.ValidatedField import ValidatedField


class EditUserFormValidator(AbstractFormValidator):

    def setRules(self):
        emailField = ValidatedField('email', False)
        emailField.addRule(
            UserValidator.email,
            'Wrong email'
        )

        return (emailField,)