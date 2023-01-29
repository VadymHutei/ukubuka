from services.LanguageService import LanguageService
from service_container import sc
from views.HTTP.ACP.Language.LanguagesView import LanguagesView


class LanguageController:

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self):
        view: LanguagesView = sc.get(LanguagesView)

        languages = self._service.get_languages()

        return view.render()