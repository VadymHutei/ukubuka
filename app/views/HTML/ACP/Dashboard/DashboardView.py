from views.web.WebView import WebView


class DashboardView(WebView):

    _page_code: str = 'acp_dashboard'

    _with_layout: bool = True