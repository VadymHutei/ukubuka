from flask import abort

from modules.ACP.view.ACPView import ACPView
from modules.ACP.view.TranslationsView import TranslationsView
from modules.ACP.view.CategoriesView import CategoriesView
from modules.Language.service.LanguageService import LanguageService
from modules.Language.validator import LanguageValidator


class ACPController:

    def __init__(self, service):
        self._service = service

    def ACPAction(self, language=None):
        view = ACPView(language=language)
        return view.render()

    def translatesAction(self, language, for_language):

        if not LanguageValidator.languageCode(for_language):
            abort(404)

        languageService = LanguageService()
        view = TranslationsView(language=language)

        translations = languageService.getTranslationsForLanguage(for_language)

        view.addData({'translations': translations})
        
        return view.render()

    def categoriesAction(self):
        categories = self._service.getCategories()
        view =  ()
        view.addData({'categories': categories})
        return view.render()