from views.web.WebView import WebView


class LayoutView(WebView):

    layout_template: str

    def __init__(self) -> None:
        super().__init__()

        self._layout_data: dict = {
            'template': self.layout_template,
        }

    def _prepare_layout_data(self) -> None:
        pass

    def _prepare_data(self) -> None:
        super()._prepare_data()

        self._prepare_layout_data()
        self._data['l'] = self._layout_data