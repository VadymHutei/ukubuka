from modules.Language.services.LanguageService import LanguageService
from modules.Language.validator import LanguageValidator
from vendor.ukubuka.AbstractFormValidator import AbstractFormValidator
from vendor.ukubuka.ValidatedField import ValidatedField


class EditTranslationFormValidator(AbstractFormValidator):

    def setRules(self):
        languageService = LanguageService.getInstance()
        fields = []

        for language in languageService.languages.values():
            fieldName = f'translation_{language.code}'
            translationField = ValidatedField(fieldName, required=True)
            translationField.addRule(
                LanguageValidator.translation,
                languageService.translate('Wrong translation')
            )
            fields.append(translationField)

        return fields