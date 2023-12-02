from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Language.EditLanguageResponseTransformer import EditLanguageResponseTransformer
from views.web.WebView import WebView


class EditLanguageView(WebView):

    _page_code = 'acp_edit_language'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        form_action = url_for(
            endpoint='.'.join((ACP_LANGUAGE_BLUEPRINT, 'edit_language_route')),
            language_code=g.current_language.code,
        )

        self._data['form'] = {
            'action': form_action,
        }

        self._data['language'] = EditLanguageResponseTransformer.transform(self._data['language'])