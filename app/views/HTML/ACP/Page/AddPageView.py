from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from views.web.WebView import WebView


class AddPageView(WebView):

    _page_code = 'acp_add_page'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        form_action = url_for(
            endpoint='.'.join((ACP_PAGE_BLUEPRINT, 'add_page_route')),
            language_code=g.current_language.code,
        )

        form = {
            'action': form_action,
        }

        self._data['form'] = form