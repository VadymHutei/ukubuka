from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from entities.Language.LanguageEntity import LanguageEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class LanguageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity | None) -> dict[str, str | int | bool | None] | None:
        if language is None:
            return None

        info_language_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.language_route',
            language_code=g.current_language.code,
            language_id=language.id,
        )
        edit_language_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.edit_language_route',
            language_code=g.current_language.code,
            code=language.code,
        )
        delete_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.delete_language_route',
            language_code=g.current_language.code,
        )

        return {
            'id': language.id,
            'code': language.code,
            'name': language.name,
            'is_active': language.is_active,
            'info_language_url': info_language_url,
            'edit_language_url': edit_language_url,
            'delete_url': delete_url,
        }