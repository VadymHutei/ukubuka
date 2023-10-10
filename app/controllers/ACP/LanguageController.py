from services.Language.LanguageService import LanguageService
from views.HTML.ACP.Language.EditLanguageView import EditLanguageView
from views.HTML.ACP.Language.LanguagesView import LanguagesView


class LanguageController:

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self) -> str:
        languages = self._service.get_all(with_inactive=True)

        view: LanguagesView = LanguagesView()

        view.set_data(languages=languages)

        return view.render()
    
    def edit_languages_page_action(self, language_code: str):
        view: EditLanguageView = EditLanguageView()

        language = self._service.find_by_code(language_code)

        view.set_data(
            language=language
        )

        if language is None:
            raise Exception
        
        return view.render()