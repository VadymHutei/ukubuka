from modules.Base.form_validators.AbstractFormValidator import AbstractFormValidator
from modules.Base.form_validators.ValidatedField import ValidatedField
from modules.Base.form_validators.ValidationRule import ValidationRule
from modules.User.validators.UserValidator import UserValidator


class EditUserFormValidator(AbstractFormValidator):

    def _set_field_validation_rules(self) -> tuple[ValidatedField]:
        ID = ValidatedField('id')
        ID.rules.append(ValidationRule(UserValidator.text_ID, 'Wrong ID'))

        email = ValidatedField('email', required=False)
        email.rules.append(ValidationRule(UserValidator.email, 'Wrong email'))

        first_name = ValidatedField('first_name', required=False, empty_allowed=True)
        first_name.rules.append(ValidationRule(UserValidator.name, 'Wrong first name'))

        last_name = ValidatedField('last_name', required=False, empty_allowed=True)
        last_name.rules.append(ValidationRule(UserValidator.name, 'Wrong last name'))

        return ID, email, first_name, last_name
