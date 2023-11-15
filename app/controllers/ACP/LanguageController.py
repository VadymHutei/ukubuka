from controllers.IController import IController
from services.Language.LanguageService import LanguageService
from views.HTML.ACP.Language.EditLanguageView import EditLanguageView
from views.HTML.ACP.Language.LanguagesView import LanguagesView


class LanguageController(IController):

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self) -> str:
        view = LanguagesView()

        view.set_data(languages=self._service.find_all())

        return view.render()
    
    def edit_language_page_action(self, language_code: str) -> str:
        view = EditLanguageView()

        view.set_data(language=self._service.find_by_code(language_code))

        return view.render()

    def delete_language_page_action(self, language_code: str):
        pass