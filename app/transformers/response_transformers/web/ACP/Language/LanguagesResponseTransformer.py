from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from entities.Language.LanguageEntity import LanguageEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class LanguagesResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity | None) -> dict[str, str | int | bool | None] | None:
        if language is None:
            return None

        info_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.language_route',
            language_code=g.current_language.code,
            language_id=language.id,
        )
        edit_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.edit_language_route',
            language_code=g.current_language.code,
            language_id=language.id,
        )
        delete_url = url_for(
            ACP_LANGUAGE_BLUEPRINT + '.delete_language_route',
            language_code=g.current_language.code,
            language_id=language.id,
        )

        return {
            'id': language.id,
            'code': language.code,
            'name': language.name,
            'is_active': language.is_active,
            'info_url': info_url,
            'edit_url': edit_url,
            'delete_url': delete_url,
        }