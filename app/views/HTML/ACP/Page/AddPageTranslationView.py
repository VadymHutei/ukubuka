from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Page.AddPageTranslationLanguageTransformer import AddPageTranslationLanguageTransformer
from views.web.WebView import WebView


class AddPageTranslationView(WebView):

    _page_code = 'acp_add_page_translation'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        form_action = url_for(
            endpoint='.'.join((ACP_PAGE_BLUEPRINT, 'add_page_translation_route')),
            language_code=g.current_language.code,
            page_id=self._data['page_id']
        )

        self._data['form'] = {
            'action': form_action,
        }

        self._data['languages'] = AddPageTranslationLanguageTransformer.transform_collection(self._data['languages'])