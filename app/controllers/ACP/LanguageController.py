from datetime import datetime
from flask import g, redirect, request, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from controllers.IController import IController
from services.Language.LanguageService import LanguageService
from value_objects.Language.LanguageVO import LanguageVO
from views.HTML.ACP.Language.AddLanguageView import AddLanguageView
from views.HTML.ACP.Language.EditLanguageView import EditLanguageView
from views.HTML.ACP.Language.LanguagesView import LanguagesView
from werkzeug import Response


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

        language_vo = LanguageVO(
            code=request.form.get('code'),
            name=request.form.get('name'),
            is_active=request.form.get('is_active') is not None,
            created_at=datetime.now(),
        )

        self._service.add_language(language_vo)

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language=g.current_language.code,
        )

        return redirect(languages_url)

    def edit_language_page_action(self, language_code: str) -> str:
        view = EditLanguageView()

        view.set_data(language=self._service.find_by_code(language_code))

        return view.render()

    def delete_language_action(self):
        self._service.delete_by_code(request.form.get('code'))

        languages_url = url_for(
            '.'.join([ACP_LANGUAGE_BLUEPRINT, 'languages_route']),
            language=g.current_language.code,
        )

        return redirect(languages_url)