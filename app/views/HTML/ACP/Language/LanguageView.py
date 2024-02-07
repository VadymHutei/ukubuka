from transformers.response_transformers.web.ACP.Language.LanguageResponseTransformer import LanguageResponseTransformer
from views.web.WebView import WebView


class LanguageView(WebView):

    _page_code = 'acp_language'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['language'] = LanguageResponseTransformer.transform(self._data['language'])