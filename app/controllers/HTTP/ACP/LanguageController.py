from services.LanguageService import LanguageService
from di_container import di_container


class LanguageController:

    def languages_page_action(self):
        language_service = di_container.get(LanguageService)
        languages = language_service.get_languages()
        print(languages)

        return 'languages page'
