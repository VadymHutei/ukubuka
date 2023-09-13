from transformers.response_transformers.Product.ProductTransformer import ProductTransformer
from views.web.WebView import WebView


class ProductView(WebView):

    _page_code: str = 'product'

    _with_layout: bool = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()
    
        self._data['product'] = ProductTransformer.transform(self._data['product'])