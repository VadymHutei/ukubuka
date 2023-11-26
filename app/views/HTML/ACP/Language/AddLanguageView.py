from flask import g, url_for

from views.web.WebView import WebView
from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT


class AddLanguageView(WebView):

    _page_code = 'acp_add_language'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        form_action = url_for(
            endpoint='.'.join((ACP_LANGUAGE_BLUEPRINT, 'add_language_route')),
            language=g.current_language.code,
        )

        self._data['form'] = {
            'action': form_action,
        }