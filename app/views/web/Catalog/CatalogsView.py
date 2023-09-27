from views.web.WebView import WebView


class CatalogsView(WebView):

    _page_code = 'catalogs'

    _with_layout = True

    # def _prepare_page_data(self) -> None:
    #     super()._prepare_page_data()
    
    #     self._data['product'] = ProductTransformer.transform(self._data['product'])