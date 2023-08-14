from typing import Type
from services.Page.PageService import PageService
from views.View import View
from views.web.WebView import WebView


class ViewFactory:

    def __init__(self, service: PageService) -> None:
        self._service = service

    def get(self, view_class: Type[View]) -> View:
        page = self._service.get_by_code(view_class.page_code)

        return view_class(page)
    
    def get_web_view(self, view_class: Type[WebView]) -> WebView:
        page = self._service.get_by_code(view_class.page_code)

        return view_class(page)