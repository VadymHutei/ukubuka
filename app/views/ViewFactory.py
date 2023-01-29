from typing import Type
from services.PageService import PageService
from views.HTTP.View import View


class ViewFactory:

    def __init__(self, service: PageService) -> None:
        self._service = service

    def get(self, view_class: Type[View]) -> View:
        page = self._service.get_by_code(view_class.page_code)

        return view_class(page)