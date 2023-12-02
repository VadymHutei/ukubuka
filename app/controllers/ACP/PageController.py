from datetime import datetime

from flask import g, redirect, request, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from controllers.IController import IController
from services.Page.PageService import PageService
from value_objects.Page.PageVO import PageVO
from views.HTML.ACP.Page.AddPageView import AddPageView
from views.HTML.ACP.Page.PageView import PageView


class PageController(IController):

    def __init__(self, service: PageService) -> None:
        self._service = service

    def pages_page_action(self):
        view = PageView()

        view.set_data(pages=self._service.get_all())

        return view.render()

    def add_page_page_action(self):
        view = AddPageView()

        return view.render()

    def add_page_action(self):
        page_vo = PageVO(
            code=request.form.get('code'),
            template=request.form.get('template'),
            layout=request.form.get('layout'),
            is_active=request.form.get('is_active') is not None,
            created_at=datetime.now(),
        )

        self._service.add_page(page_vo)

        pages_url = url_for(
            '.'.join([ACP_PAGE_BLUEPRINT, 'pages_route']),
            language_code=g.current_language.code,
        )

        return redirect(pages_url)