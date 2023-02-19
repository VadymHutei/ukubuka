from services.LanguageService import LanguageService
from service_container import sc
from views.HTML.ACP.Language.LanguagesView import LanguagesView
from views.ViewFactory import ViewFactory


class LanguageController:

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self) -> str:
        view_factory = sc.get(ViewFactory)
        view: LanguagesView = view_factory.get(LanguagesView)

        languages = self._service.get_languages()

        view.set_data(
            languages=languages
        )

        return view.render()