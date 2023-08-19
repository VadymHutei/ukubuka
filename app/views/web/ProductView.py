from views.web.WebView import WebView


class ProductView(WebView):

    _page_code: str = 'product'

    _with_layout: bool = True