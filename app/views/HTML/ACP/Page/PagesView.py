from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Page.PagesResponseTransformer import PagesResponseTransformer
from views.web.WebView import WebView


class PagesView(WebView):

    _page_code = 'acp_pages'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        add_url = url_for(
            endpoint='.'.join((ACP_PAGE_BLUEPRINT, 'add_page_route')),
            language_code=g.current_language.code,
        )

        self._data['pages'] = PagesResponseTransformer.transform_collection(self._data['pages'])
        self._data['add_url'] = add_url