from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Language.EditLanguageResponseTransformer import EditLanguageResponseTransformer
from views.HTML.ACP.ACPLayoutView import ACPLayoutView


class EditLanguageView(ACPLayoutView):

    _page_code: str = 'acp_edit_language'

    _with_layout: bool = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['form'] = {
            'action': url_for(
                endpoint='.'.join((ACP_LANGUAGE_BLUEPRINT, 'edit_language_route')),
                language=g.current_language.code,
                language_code=self._data['language'].code,
            ),
        }

        self._data['language'] = EditLanguageResponseTransformer.transform(self._data['language'])