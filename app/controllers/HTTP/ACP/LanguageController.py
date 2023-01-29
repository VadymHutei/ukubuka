from services.LanguageService import LanguageService
from service_container import sc
from views.ACP.Language.LanguagesView import LanguagesView


class LanguageController:

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self):
        languages = self._service.get_languages()
        view = sc.get(LanguagesView)

        return languages
