from entities.Page.PageEntity import PageEntity
from views.HTML.HTMLView import HTMLView


class LayoutView(HTMLView):

    layout_template: str

    def __init__(self, page: PageEntity) -> None:
        super().__init__(page)

        self._layout_data: dict = {
            'template': self.layout_template,
        }

    def _prepare_layout_data(self) -> None:
        pass

    def _prepare_data(self) -> None:
        super()._prepare_data()

        self._prepare_layout_data()
        self._data['l'] = self._layout_data