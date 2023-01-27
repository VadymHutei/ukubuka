from services.LanguageService import LanguageService


class LanguageController:

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self):
        languages = self._service.get_languages()
        print(languages)

        return 'languages page'
