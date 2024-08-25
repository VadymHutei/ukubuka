from views.web.WebView import WebView


class CatalogsView(WebView):

    _page_code = 'catalogs_page'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()
