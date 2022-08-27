from modules.Base.form_validators.AbstractFormValidator import AbstractFormValidator
from modules.Base.form_validators.ValidatedField import ValidatedField
from modules.Base.form_validators.ValidationRule import ValidationRule
from modules.User.validators.UserValidator import UserValidator


class EditUserFormValidator(AbstractFormValidator):

    def _setFieldValidationRules(self):
        ID = ValidatedField('id', required=True)
        ID.addRule(ValidationRule(UserValidator.text_ID, 'Wrong ID'))

        email = ValidatedField('email', required=False)
        email.addRule(ValidationRule(UserValidator.email, 'Wrong email'))

        password = ValidatedField('password', required=False)
        password.addRule(ValidationRule(UserValidator.password, 'Wrong password'))

        first_name = ValidatedField('first_name', required=False, emptyAllowed=True)
        first_name.addRule(ValidationRule(UserValidator.name, 'Wrong first name'))

        last_name = ValidatedField('last_name', required=False, emptyAllowed=True)
        last_name.addRule(ValidationRule(UserValidator.name, 'Wrong last name'))

        return ID, email, password, first_name, last_name
