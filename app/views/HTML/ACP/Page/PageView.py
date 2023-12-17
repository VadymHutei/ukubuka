from flask import url_for, g

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Page.PageResponseTransformer import PageResponseTransformer
from transformers.response_transformers.web.ACP.Page.PageTextResponseTransformer import PageTextResponseTransformer
from views.web.WebView import WebView


class PageView(WebView):

    _page_code = 'acp_page'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['page'] = PageResponseTransformer.transform(self._data['page'])
        self._data['page']['translations'] = PageTextResponseTransformer.transform_collection(
            self._data['page_translations']
        )

        languages = {language.id: language.name for language in self._data['languages']}
        for translation in self._data['page']['translations']:
            edit_url = url_for(
                ACP_PAGE_BLUEPRINT + '.edit_page_translation_route',
                language_code=g.current_language.code,
                id=translation['id'],
            )

            translation['language'] = languages[translation['language_id']].capitalize()
            translation['edit_url'] = edit_url
