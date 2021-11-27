from flask import request, redirect, url_for

from modules.Language.form_validators.EditTranslationFormValidator import EditTranslationFormValidator
from modules.Language.service import LanguageService
from modules.Language.validator import LanguageValidator
from modules.Language.views.ACPTranslationEditView import ACPTranslationEditView
from modules.Language.views.ACPTranslationView import ACPTranslationView


class ACPTranslationController:

    def listAction(self):
        view = ACPTranslationView()
        languageService = LanguageService.getInstance()

        view.data = {'texts': languageService.texts}

        return view.render()

    def editPageAction(self):
        view = ACPTranslationEditView()
        languageService = LanguageService.getInstance()

        view.data = {'text': languageService.getTextByID(request.args.get('id'))}

        return view.render()

    def editAction(self):
        textID = int(request.args.get('id', 0))
        if (textID == 0 or not LanguageValidator.intID(textID, True)):
            return redirect(url_for('ACPTranslationPage', language=request.ctx['language']))

        languageService = LanguageService.getInstance()

        view = ACPTranslationEditView()
        
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