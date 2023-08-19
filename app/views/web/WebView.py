from flask import render_template

from views.View import View
from service_container import sc
from services.Page.PageService import PageService
from entities.Page.PageEntity import PageEntity


class WebView(View):

    _page_code: str

    def __init__(self) -> None:
        super().__init__()

        self._page_service = sc.get(PageService)
        self._page: PageEntity = self._page_service.get_by_code(self._page_code)

        self._template_data: dict = {}

    def _prepare_data(self) -> None:
        self._prepare_page_data()

        self._prepare_template_data()
        self._data['t'] = self._template_data

    def _prepare_page_data(self) -> None:
        pass

    def _prepare_template_data(self) -> None:
        self._template_data['title'] = self._page.title

    def set_data(self, **data) -> None:
        self._data.update(data)

    def render(self) -> str:
        self._prepare_data()

        return render_template(self._page.template, **self._data)