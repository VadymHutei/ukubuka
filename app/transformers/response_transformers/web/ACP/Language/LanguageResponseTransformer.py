from flask import g, url_for

from blueprints.blueprint_names import ACP_LANGUAGE_BLUEPRINT
from entities.Language.LanguageEntity import LanguageEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class LanguageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity | None) -> dict[str, str | int | bool | None] | None:
        if language is None:
            return None

        created_at = language.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = language.updated_at.strftime(cls.ACP_DATE_FORMAT) if language.updated_at else None
        deleted_at = language.deleted_at.strftime(cls.ACP_DATE_FORMAT) if language.deleted_at else None

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
            'created_at': created_at,
            'updated_at': updated_at,
            'deleted_at': deleted_at,
            'edit_url': edit_url,
            'delete_url': delete_url,
        }