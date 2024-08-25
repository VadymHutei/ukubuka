from views.web.WebView import WebView


class HomeView(WebView):

    _page_code = 'home_page'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()
