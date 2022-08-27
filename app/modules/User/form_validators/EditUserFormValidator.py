from modules.Base.form_validators.AbstractFormValidator import AbstractFormValidator
from modules.Base.form_validators.ValidatedField import ValidatedField
from modules.Base.form_validators.ValidationRule import ValidationRule
from modules.User.validators.UserValidator import UserValidator


class EditUserFormValidator(AbstractFormValidator):

    def _set_field_validation_rules(self):
        ID = ValidatedField('id', required=True)
        ID.add_rule(ValidationRule(UserValidator.text_ID, 'Wrong ID'))

        email = ValidatedField('email', required=False)
        email.add_rule(ValidationRule(UserValidator.email, 'Wrong email'))

        password = ValidatedField('password', required=False)
        password.add_rule(ValidationRule(UserValidator.password, 'Wrong password'))

        first_name = ValidatedField('first_name', required=False, empty_allowed=True)
        first_name.add_rule(ValidationRule(UserValidator.name, 'Wrong first name'))

        last_name = ValidatedField('last_name', required=False, empty_allowed=True)
        last_name.add_rule(ValidationRule(UserValidator.name, 'Wrong last name'))

        return ID, email, password, first_name, last_name
