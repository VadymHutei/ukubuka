from flask import g, url_for
from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from views.HTTP.ACP.ACPLayoutView import ACPLayoutView
from entities.transformers.HTTP.ACP.LanguageTransformer import LanguageTransformer


class LanguagesView(ACPLayoutView):

    page_code: str = 'acp_languages'

    def _prepare_page_data(self) -> None:
        super()._prepare_page_data()

        self._data['languages'] = LanguageTransformer.transform_dict(self._data['languages'])

        for code in self._data['languages']:
            edit_link = url_for(
                f'{ACP_LANGUAGE_BLUEPRINT}.edit_language_route',
                language=g.current_language.code,
                language_code=code
            )
            delete_link = url_for(
                f'{ACP_LANGUAGE_BLUEPRINT}.delete_language_route',
                language=g.current_language.code,
                language_code=code
            )
            self._data['languages'][code]['links'] = {
                'edit': edit_link,
                'delete': delete_link,
            }

        print(self._data['languages'])