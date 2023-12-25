from flask import g, redirect, request, url_for, abort

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from controllers.IController import IController
from services.Language.LanguageService import LanguageService
from services.Page.PageService import PageService
from transformers.request_transformers.Page.AddPageDTOTransformer import AddPageDTOTransformer
from transformers.request_transformers.Page.RequestToUpdatePageDTOTransformer import RequestToUpdatePageDTOTransformer
from transformers.request_transformers.Page.RequestToUpdatePageTranslationDTOTransformer import \
    RequestToUpdatePageTranslationDTOTransformer
from views.HTML.ACP.Page.AddPageTranslationView import AddPageTranslationView
from views.HTML.ACP.Page.AddPageView import AddPageView
from views.HTML.ACP.Page.EditPageTranslationView import EditPageTranslationView
from views.HTML.ACP.Page.EditPageView import EditPageView
from views.HTML.ACP.Page.PageView import PageView
from views.HTML.ACP.Page.PagesView import PagesView


class PageController(IController):

    def __init__(self, service: PageService, language_service: LanguageService):
        self._service = service
        self._language_service = language_service

    def pages_page_action(self):
        view = PagesView()

        view.set_data(pages=self._service.find_all())

        return view.render()

    def page_page_action(self):
        page_code = request.args.get('code')

        if page_code is None:
            pages_url = url_for(
                '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
                language_code=g.current_language.code,
            )

            return redirect(pages_url)

        page = self._service.find_by_code(page_code)

        if page is None:
            abort(404)

        view = PageView()

        view.set_data(
            page=page,
            page_translations=self._service.find_translations_by_code(page_code),
            languages=self._language_service.find_all()
        )

        return view.render()

    def add_page_page_action(self):
        view = AddPageView()

        return view.render()

    def add_page_action(self):
        add_page_dto = AddPageDTOTransformer.transform(request)

        self._service.add_page(add_page_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def edit_page_page_action(self):
        view = EditPageView()

        page = self._service.find_by_code(request.args.get('code'))

        view.set_data(page=page)

        return view.render()

    def edit_page_action(self):
        update_page_dto = RequestToUpdatePageDTOTransformer.transform(request)

        self._service.update_page(update_page_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def delete_page_action(self):
        self._service.delete_by_code(request.form.get('code'))

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def add_page_translation_page_action(self):
        view = AddPageTranslationView()

        return view.render()

    def add_page_translation_action(self):
        update_page_translation_dto = RequestToUpdatePageTranslationDTOTransformer.transform(request)

        self._service.update_page_translation(update_page_translation_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def edit_page_translation_page_action(self):
        view = EditPageTranslationView()

        translation = self._service.find_translation_by_id(int(request.args.get('id')))

        view.set_data(translation=translation)

        return view.render()

    def edit_page_translation_action(self):
        update_page_translation_dto = RequestToUpdatePageTranslationDTOTransformer.transform(request)

        self._service.update_page_translation(update_page_translation_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)
