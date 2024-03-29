from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Page.AddPageTranslationLanguageTransformer import AddPageTranslationLanguageTransformer
from transformers.response_transformers.web.ACP.Page.EditPageTranslationResponseTransformer import EditPageTranslationResponseTransformer
from views.web.WebView import WebView


class EditPageTranslationView(WebView):

    _page_code = 'acp_edit_page_translation'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        form_action = url_for(
            endpoint='.'.join((ACP_PAGE_BLUEPRINT, 'edit_page_translation_route')),
            language_code=g.current_language.code,
            translation_id=self._data['translation'].id,
        )

        self._data['form'] = {
            'action': form_action,
        }

        self._data['translation'] = EditPageTranslationResponseTransformer.transform(self._data['translation'])
        self._data['languages'] = AddPageTranslationLanguageTransformer.transform_collection(self._data['languages'])