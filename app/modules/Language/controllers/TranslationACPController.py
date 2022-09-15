import re

from flask import g, redirect, request, url_for
from modules.Language.form_validators.EditTranslationFormValidator import EditTranslationFormValidator
from modules.Language.services.LanguageService import LanguageService
from modules.Language.validators.LanguageValidator import LanguageValidator
from modules.Language.views.EditTranslationACPView import EditTranslationACPView
from modules.Language.views.TranslationsACPView import TranslationsACPView


class TranslationACPController:

    def __init__(self):
        self._languageService = LanguageService()

    def translationsPageAction(self):
        view = TranslationsACPView()

        view.data = {'texts': g.t.texts}

        return view.render()

    def editTranslationsPageAction(self):
        textID = int(request.args.get('id', 0))

        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(
                url_for(
                    'translationsACPBlueprint.translationsACPRoute',
                    language=g.current_language.code
                )
            )

        text = self._languageService.getTextByID(textID)

        if text is None:
            return redirect(
                url_for(
                    'translationsACPBlueprint.translationsACPRoute',
                    language=g.current_language.code
                )
            )

        view = EditTranslationACPView()
        view.data = {'text': text}

        return view.render()

    def editTranslationsAction(self):
        textID = int(request.args.get('id', 0))

        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(
                url_for(
                    'translationsACPBlueprint.translationsACPRoute',
                    language=g.current_language.code
                )
            )

        textEntity = self._languageService.getTextByID(textID)

        if textEntity is None:
            return redirect(
                url_for(
                    'translationsACPBlueprint.translationsACPRoute',
                    language=g.current_language.code
                )
            )

        formValidator = EditTranslationFormValidator(request.form)
        if formValidator.errors:
            view = EditTranslationACPView()
            view.error('Form errors')
            view.data = {
                'text': textEntity,
                'formErrors': formValidator.errors,
            }

            return view.render()

        data = formValidator.getFormData()

        pattern = re.compile('translation_(' + '|'.join(g.t.languages.keys()) + ')')
        for fieldName, fieldValue in data.items():
            result = pattern.search(fieldName)
            if result:
                language = result.group(1)
                if language not in g.t.languages:
                    continue
                textEntity.translations[language] = fieldValue

        self._languageService.updateTextTranslations(textEntity)
        g.t.setTexts()

        return redirect(
            url_for(
                'translationsACPBlueprint.translationsACPRoute',
                language=g.current_language.code
            )
        )

    def deleteTextAction(self):
        textID = int(request.args.get('id', 0))

        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(
                url_for(
                    'translationsACPBlueprint.translationsACPRoute',
                    language=g.current_language.code
                )
            )

        self._languageService.deleteTranslations(textID)
        self._languageService.deleteText(textID)
        g.t.setTexts()

        return redirect(
            url_for(
                'translationsACPBlueprint.translationsACPRoute',
                language=g.current_language.code
            )
        )
