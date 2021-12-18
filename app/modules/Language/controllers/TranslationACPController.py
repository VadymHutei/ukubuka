from flask import request, redirect, url_for

from modules.Language.form_validators.EditTranslationFormValidator import EditTranslationFormValidator
from modules.Language.services.LanguageService import LanguageService
from modules.Language.validators.LanguageValidator import LanguageValidator
from modules.Language.views.EditTranslationACPView import EditTranslationACPView
from modules.Language.views.TranslationsACPView import TranslationsACPView


class TranslationACPController:

    def translationsPageAction(self):
        view = TranslationsACPView()
        languageService = LanguageService.getInstance()

        view.data = {'texts': languageService.texts}

        return view.render()

    def editTranslationsPageAction(self):
        view = EditTranslationACPView()
        languageService = LanguageService.getInstance()

        view.data = {'text': languageService.getTextByID(request.args.get('id'))}

        return view.render()

    def editTranslationsAction(self):
        textID = int(request.args.get('id', 0))

        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(url_for('translationsACPBlueprint.translationsACPRoute', language=request.ctx['language'].code))

        languageService = LanguageService.getInstance()
        
        formValidator = EditTranslationFormValidator(request.form)
        if formValidator.hasErrors:
            view = EditTranslationACPView()
            view.error('Form errors')
            view.data = {'text': languageService.getTextByID(textID)}
            view.data = {'formErrors': formValidator.errors}
            return view.render()

        data = formValidator.getFormData()
        data['textID'] = textID
        languageService.updateTranslations(data)

        return redirect(url_for('translationsACPBlueprint.translationsACPRoute', language=request.ctx['language'].code))

    def deleteTextAction(self):
        textID = int(request.args.get('id', 0))

        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(url_for('translationsACPBlueprint.translationsACPRoute', language=request.ctx['language'].code))

        languageService = LanguageService.getInstance()

        languageService.deleteTranslations(textID)
        languageService.deleteText(textID)

        return redirect(url_for('translationsACPBlueprint.translationsACPRoute', language=request.ctx['language'].code))