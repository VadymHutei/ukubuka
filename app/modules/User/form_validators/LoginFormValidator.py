from modules.Base.form_validators.AbstractFormValidator import AbstractFormValidator
from modules.Base.form_validators.ValidatedField import ValidatedField
from modules.Base.form_validators.ValidationRule import ValidationRule
from modules.User.validators.UserValidator import UserValidator


class LoginFormValidator(AbstractFormValidator):

    def _set_field_validation_rules(self):
        email = ValidatedField('email', required=True)
        email.rules.append(ValidationRule(UserValidator.email, 'Wrong email'))

        password = ValidatedField('password', required=True)
        password.rules.append(ValidationRule(
            UserValidator.password, 'Wrong password'))

        return email, password
