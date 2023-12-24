from flask import render_template

from entities.Page.PageEntity import PageEntity
from service_container import sc
from services.Page.PageService import PageService
from views.View import View


class WebView(View):

    _page_code: str

    _with_layout: bool = False

    def __init__(self) -> None:
        super().__init__()

        self._page_data: dict = {}
        self._template_data: dict = {}

    def _prepare_data(self) -> None:
        self._prepare_page_data()
        self._data['p'] = self._page_data

        self._prepare_template_data()
        self._data['t'] = self._template_data

    def _prepare_page_data(self) -> None:
        self._set_page()

        self._page_data['template'] = self._page.template
        self._page_data['title'] = self._page.title

    def _prepare_template_data(self) -> None:
        self._template_data['title'] = self._page.title
        self._template_data['layout'] = self._page.layout

    def _set_page(self) -> None:
        page_service: PageService = sc.get(PageService)

        self._page: PageEntity = page_service.find_by_code(self._page_code)

    def set_data(self, **data) -> None:
        self._data.update(data)

    def render(self) -> str:
        self._prepare_data()

        if self._with_layout:
            return render_template('include_layout.html', **self._data)
        else:
            return render_template(self._page.template, **self._data)