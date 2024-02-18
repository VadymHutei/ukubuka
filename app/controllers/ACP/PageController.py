from flask import g, redirect, request, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from controllers.IController import IController
from services.Language.LanguageService import LanguageService
from services.Page.PageService import PageService
from transformers.request_transformers.Page.AddPageDTOTransformer import AddPageDTOTransformer
from transformers.request_transformers.Page.AddPageTranslationDTOTransformer import AddPageTranslationDTOTransformer
from transformers.request_transformers.Page.EditPageDTOTransformer import EditPageDTOTransformer
from transformers.request_transformers.Page.EditPageTranslationDTOTransformer import EditPageTranslationDTOTransformer
from views.HTML.ACP.Page.AddPageTranslationView import AddPageTranslationView
from views.HTML.ACP.Page.AddPageView import AddPageView
from views.HTML.ACP.Page.EditPageTranslationView import EditPageTranslationView
from views.HTML.ACP.Page.EditPageView import EditPageView
from views.HTML.ACP.Page.PageView import PageView
from views.HTML.ACP.Page.PagesView import PagesView


class PageController(IController):

    def __init__(self, page_service: PageService, language_service: LanguageService):
        self._page_service = page_service
        self._language_service = language_service

    def pages_page_action(self):
        view = PagesView()

        view.set_data(pages=self._page_service.find_all())

        return view.render()

    def page_page_action(self, page_id: int):
        page = self._page_service.find(page_id)

        view = PageView()

        view.set_data(
            page=page,
            page_translations=self._page_service.find_translations_by_page_id(page_id),
            languages=self._language_service.find_all()
        )

        return view.render()

    def add_page_page_action(self):
        view = AddPageView()

        return view.render()

    def add_page_action(self):
        add_page_dto = AddPageDTOTransformer.transform(request)

        self._page_service.add_page(add_page_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def edit_page_page_action(self, page_id: int):
        page = self._page_service.find(page_id)

        view = EditPageView()

        view.set_data(page=page)

        return view.render()

    def edit_page_action(self, page_id: int):
        edit_page_dto = EditPageDTOTransformer.transform(request)

        self._page_service.edit_page(page_id, edit_page_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'page_route']),
            language_code=g.current_language.code,
            page_id=page_id,
        )

        return redirect(pages_url)

    def delete_page_action(self, page_id: int):
        self._page_service.delete(page_id)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def add_page_translation_page_action(self, page_id: int):
        languages = self._language_service.find_all()

        view = AddPageTranslationView()

        view.set_data(
            page_id=page_id,
            languages=languages,
        )

        return view.render()

    def add_page_translation_action(self, page_id: int):
        add_page_translation_dto = AddPageTranslationDTOTransformer.transform(request)

        self._page_service.add_page_translation(page_id, add_page_translation_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'page_route']),
            language_code=g.current_language.code,
            page_id=page_id,
        )

        return redirect(pages_url)

    def edit_page_translation_page_action(self, translation_id: int):
        languages = self._language_service.find_all()

        translation = self._page_service.find_translation(translation_id)

        view = EditPageTranslationView()

        view.set_data(
            languages=languages,
            translation=translation,
        )

        return view.render()

    def edit_page_translation_action(self, translation_id: int):
        update_page_translation_dto = EditPageTranslationDTOTransformer.transform(request)

        self._page_service.edit_page_translation(translation_id, update_page_translation_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)
