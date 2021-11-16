from flask import request

from modules.Language.views.ACPTranslationView import ACPTranslationView
from modules.Language.views.ACPTranslationEditView import ACPTranslationEditView
from modules.Language.service import LanguageService


class ACPTranslationController:

    def listAction(self):
        view = ACPTranslationView()
        languageService = LanguageService.getInstance()

        view.data = {'texts': languageService.texts}

        return view.render()

    def editAction(self):
        if request.method == 'GET':
            view = ACPTranslationEditView()
            languageService = LanguageService.getInstance()

            view.data = {'text': languageService.getTextByID(request.args.get('id'))}

            return view.render()
        elif request.method == 'POST':
            return 'in progress'