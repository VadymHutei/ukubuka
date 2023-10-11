from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from entities.Language.LanguageEntity import LanguageEntity
from response_transformers.web.WebResponseTransformer import WebResponseTransformer


class LanguageResponseTransformer(WebResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity) -> dict[str, str|int]:
        edit_page_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.edit_language_route',
            language=g.current_language.code,
            language_code=language.code,
        )
        delete_page_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.delete_language_route',
            language=g.current_language.code,
            language_code=language.code,
        )

        return {
            'id': language.id,
            'code': language.code,
            'name': language.name,
            'is_active': cls.checkbox(language.is_active),
            'edit_page_url': edit_page_url,
            'delete_page_url': delete_page_url,
        }