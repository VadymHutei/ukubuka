from views.web.Product.transformers.ProductViewTransformer import ProductViewTransformer
from views.web.WebView import WebView


class ProductView(WebView):

    _page_code = 'product_page'

    _with_layout: bool = True

    def __init__(self) -> None:
        super().__init__()

        self._productViewTransformer = ProductViewTransformer()

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['product'] = self._productViewTransformer.transform(self._data['product'])
