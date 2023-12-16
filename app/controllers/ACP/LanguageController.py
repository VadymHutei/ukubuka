from flask import g, redirect, request, url_for
from werkzeug import Response

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from controllers.IController import IController
from data_transfer_objects.Language.AddLanguageDTO import AddLanguageDTO
from data_transfer_objects.Language.UpdateLanguageDTO import UpdateLanguageDTO
from services.Language.LanguageService import LanguageService
from transformers.request_transformers.Language.AddLanguageDTOTransformer import AddLanguageDTOTransformer
from transformers.request_transformers.Language.UpdateLanguageDTOTransformer import UpdateLanguageDTOTransformer
from views.HTML.ACP.Language.AddLanguageView import AddLanguageView
from views.HTML.ACP.Language.EditLanguageView import EditLanguageView
from views.HTML.ACP.Language.LanguagesView import LanguagesView


class LanguageController(IController):

    def __init__(self, service: LanguageService) -> None:
        self._service: LanguageService = service

    def languages_page_action(self) -> str:
        view = LanguagesView()

        view.set_data(languages=self._service.find_all())

        return view.render()

    def add_language_page_action(self) -> str:
        view = AddLanguageView()

        return view.render()

    def add_language_action(self) -> Response:
        add_language_dto = AddLanguageDTOTransformer.transform(request)

        self._service.add(add_language_dto)

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language_code=g.current_language.code,
        )

        return redirect(languages_url)

    def edit_language_page_action(self) -> str:
        view = EditLanguageView()

        view.set_data(language=self._service.find_by_code(request.args.get('code')))

        return view.render()

    def edit_language_action(self) -> Response:
        update_language_dto = UpdateLanguageDTOTransformer.transform(request)

        self._service.update(update_language_dto)

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language_code=g.current_language.code,
        )

        return redirect(languages_url)

    def delete_language_action(self) -> Response:
        self._service.delete_by_code(request.form.get('code'))

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language_code=g.current_language.code,
        )

        return redirect(languages_url)