from views.web.WebView import WebView


class CatalogView(WebView):

    _page_code = 'catalog'

    _with_layout: bool = True

    # def _prepare_page_data(self) -> None:
    #     super()._prepare_page_data()
    
    #     self._data['product'] = ProductTransformer.transform(self._data['product'])