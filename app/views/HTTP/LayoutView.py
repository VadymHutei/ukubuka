from entities.PageEntity import PageEntity
from views.HTTP.View import View


class LayoutView(View):

    layout_template: str

    def __init__(self, page: PageEntity) -> None:
        super().__init__(page)

        self._layout_data = {
            'template': self.layout_template,
        }

    def _prepare_layout_data(self):
        pass

    def _prepare_data(self):
        super()._prepare_data()

        self._prepare_layout_data()
        self._data['l'] = self._layout_data