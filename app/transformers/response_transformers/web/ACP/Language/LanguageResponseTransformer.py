from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from entities.Language.LanguageEntity import LanguageEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class LanguageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity | None) -> dict[str, str | int | bool | None] | None:
        if language is None:
            return None

        created_at = language.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = language.updated_at.strftime(cls.ACP_DATE_FORMAT) if language.updated_at else None
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
            'is_active': language.is_active,
            'created_at': created_at,
            'updated_at': updated_at,
            'edit_page_url': edit_page_url,
            'delete_page_url': delete_page_url,
        }