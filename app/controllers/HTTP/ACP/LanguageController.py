from services.LanguageService import LanguageService


class LanguageController:

    def languages_page_action(self):
        language_service = LanguageService()
        languages = language_service.get_languages()

        return 'languages page'
