from flask import g, redirect, request, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from controllers.IController import IController
from services.Language.LanguageService import LanguageService
from transformers.request_transformers.Language.AddLanguageDTOTransformer import AddLanguageDTOTransformer
from transformers.request_transformers.Language.EditLanguageDTOTransformer import EditLanguageDTOTransformer
from views.HTML.ACP.Language.AddLanguageView import AddLanguageView
from views.HTML.ACP.Language.EditLanguageView import EditLanguageView
from views.HTML.ACP.Language.LanguagesView import LanguagesView
from views.HTML.ACP.Language.LanguageView import LanguageView


class LanguageController(IController):

    def __init__(self, language_service: LanguageService):
        self._language_service: LanguageService = language_service

    def languages_page_action(self):
        view = LanguagesView()

        view.set_data(languages=self._language_service.find_all())

        return view.render()

    def language_page_action(self, language_id: int):
        view = LanguageView()

        view.set_data(language=self._language_service.find(language_id))

        return view.render()

    def add_language_page_action(self):
        view = AddLanguageView()

        return view.render()

    def add_language_action(self):
        add_language_dto = AddLanguageDTOTransformer.transform(request)

        self._language_service.add(add_language_dto)

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language_code=g.current_language.code,
        )

        return redirect(languages_url)

    def edit_language_page_action(self, language_id: int):
        view = EditLanguageView()

        view.set_data(language=self._language_service.find(language_id))

        return view.render()

    def edit_language_action(self, language_id: int):
        edit_language_dto = EditLanguageDTOTransformer.transform(request)

        self._language_service.edit_language(language_id, edit_language_dto)

        language_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'language_route']),
            language_code=g.current_language.code,
            language_id=language_id,
        )

        return redirect(language_url)

    def delete_language_action(self, language_id: int):
        self._language_service.delete(language_id)

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language_code=g.current_language.code,
        )

        return redirect(languages_url)