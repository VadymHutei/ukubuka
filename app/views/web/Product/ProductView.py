from services.Page.PageService import PageService
from views.web.Product.transformers.ProductViewTransformer import ProductViewTransformer
from views.web.WebView import WebView


class ProductView(WebView):

    _page_code = 'product_page'

    _with_layout: bool = True

    def __init__(self, page_service: PageService, product_transformer: ProductViewTransformer) -> None:
        super().__init__(page_service)

        self._productViewTransformer = product_transformer

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['product'] = self._productViewTransformer.transform(self._data['product'])
