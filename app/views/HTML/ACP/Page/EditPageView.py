from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from transformers.response_transformers.web.ACP.Page.EditPageResponseTransformer import EditPageResponseTransformer
from views.web.WebView import WebView


class EditPageView(WebView):

    _page_code = 'acp_edit_page'

    _with_layout = True

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        form_action = url_for(
            endpoint='.'.join((ACP_PAGE_BLUEPRINT, 'edit_page_route')),
            language_code=g.current_language.code,
            page_id=self._data['page'].id
        )

        form = {
            'action': form_action,
        }

        self._data['form'] = form
        self._data['page'] = EditPageResponseTransformer.transform(self._data['page'])