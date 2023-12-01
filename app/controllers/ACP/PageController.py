from controllers.IController import IController
from services.Page.PageService import PageService
from views.HTML.ACP.Page.PageView import PageView


class PageController(IController):

    def __init__(self, service: PageService) -> None:
        self._service = service

    def pages_page_action(self):
        view = PageView()

        view.set_data(pages=self._service.get_all())

        return view.render()