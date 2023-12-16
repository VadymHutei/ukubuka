from flask import g, redirect, request, url_for
from werkzeug import Response

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from controllers.IController import IController
from services.Page.PageService import PageService
from transformers.request_transformers.Page.RequestToAddPageDTOTransformer import RequestToAddPageDTOTransformer
from transformers.request_transformers.Page.RequestToUpdatePageDTOTransformer import RequestToUpdatePageDTOTransformer
from views.HTML.ACP.Page.AddPageView import AddPageView
from views.HTML.ACP.Page.EditPageView import EditPageView
from views.HTML.ACP.Page.PageView import PageView


class PageController(IController):

    def __init__(self, service: PageService) -> None:
        self._service = service

    def pages_page_action(self) -> str:
        view = PageView()

        view.set_data(pages=self._service.get_all())

        return view.render()

    def add_page_page_action(self) -> str:
        view = AddPageView()

        return view.render()

    def add_page_action(self) -> Response:
        add_page_dto = RequestToAddPageDTOTransformer.transform(request)

        self._service.add_page(add_page_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def edit_page_page_action(self) -> str:
        view = EditPageView()

        page = self._service.find_page_by_code(request.args.get('code'))

        view.set_data(page=page)

        return view.render()

    def edit_page_action(self) -> Response:
        update_page_dto = RequestToUpdatePageDTOTransformer.transform(request)

        self._service.update_page(update_page_dto)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)

    def delete_page_action(self) -> Response:
        self._service.delete_page_by_code(request.form.get('code'))

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)