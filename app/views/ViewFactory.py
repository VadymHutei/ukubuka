from typing import Type
from services.PageService import PageService
from views.HTML.HTMLView import HTMLView


class ViewFactory:

    def __init__(self, service: PageService) -> None:
        self._service = service

    def get(self, view_class: Type[HTMLView]) -> HTMLView:
        page = self._service.get_by_code(view_class.page_code)

        return view_class(page)