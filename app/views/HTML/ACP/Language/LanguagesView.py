from response_transformers.web.ACP.Language.LanguageResponseTransformer import LanguageResponseTransformer
from views.web.WebView import WebView


class LanguagesView(WebView):

    _page_code: str = 'acp_languages'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['languages'] = LanguageResponseTransformer.collection(self._data['languages'])