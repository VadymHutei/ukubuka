from flask import g
from modules.Base.form_validators.AbstractFormValidator import AbstractFormValidator
from modules.Base.form_validators.ValidatedField import ValidatedField
from modules.Language.validators.LanguageValidator import LanguageValidator


class EditTranslationFormValidator(AbstractFormValidator):

    def _setFieldValidationRules(self):
        fields = []

        for languageCode in g.t.languages:
            fieldName = f'translation_{languageCode}'
            translationField = ValidatedField(fieldName, required=True)
            translationField.addRule(LanguageValidator.translation, g.t._('Wrong translation'))
            fields.append(translationField)

        return fields
