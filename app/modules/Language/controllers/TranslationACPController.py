from flask import request, redirect, url_for

from modules.Language.form_validators.EditTranslationFormValidator import EditTranslationFormValidator
from modules.Language.services.LanguageService import LanguageService
from modules.Language.validator import LanguageValidator
from modules.Language.views.EditTranslationACPView import EditTranslationACPView
from modules.Language.views.TranslationsACPView import TranslationsACPView


class TranslationACPController:

    def translationsAction(self):
        view = TranslationsACPView()
        languageService = LanguageService.getInstance()

        view.data = {'texts': languageService.texts}

        return view.render()

    def editPageAction(self):
        view = EditTranslationACPView()
        languageService = LanguageService.getInstance()

        view.data = {'text': languageService.getTextByID(request.args.get('id'))}

        return view.render()

    def editAction(self):
        textID = int(request.args.get('id', 0))
        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(url_for('TranslationACPPage', language=request.ctx['language']))

        languageService = LanguageService.getInstance()

        view = EditTranslationACPView()
        
        formValidator = EditTranslationFormValidator(request.form)
        if formValidator.hasErrors:
            view.error('Form errors')
            view.data = {'text': languageService.getTextByID(textID)}
            view.data = {'formErrors': formValidator.errors}
            return view.render()

        data = formValidator.getFormData()
        data['textID'] = textID
        languageService.updateTranslations(data)
        
        view.data = {'text': languageService.getTextByID(textID)}
        
        return view.render()