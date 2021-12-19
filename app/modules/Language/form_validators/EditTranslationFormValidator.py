from flask import g

from modules.Language.validators.LanguageValidator import LanguageValidator
from vendor.ukubuka.AbstractFormValidator import AbstractFormValidator
from vendor.ukubuka.ValidatedField import ValidatedField


class EditTranslationFormValidator(AbstractFormValidator):

    def setRules(self):
        fields = []

        for languageCode in g.t.languages:
            fieldName = f'translation_{languageCode}'
            translationField = ValidatedField(fieldName, required=True)
            translationField.addRule(
                LanguageValidator.translation,
                g.t._('Wrong translation')
            )
            fields.append(translationField)

        return fields