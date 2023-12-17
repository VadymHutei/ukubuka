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
            translation['language'] = languages[translation['language_id']].capitalize()
