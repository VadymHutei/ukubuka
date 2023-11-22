from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Language.LanguageResponseTransformer import LanguageResponseTransformer
from views.web.WebView import WebView


class LanguagesView(WebView):

    _page_code = 'acp_languages'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        add_language_url = url_for(
            endpoint='.'.join((ACP_LANGUAGE_BLUEPRINT, 'add_language_route')),
            language=g.current_language.code,
        )

        self._data['languages'] = LanguageResponseTransformer.transform_collection(self._data['languages'])
        self._data['add_language_url'] = add_language_url