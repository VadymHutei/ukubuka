from entities.Language.LanguageEntity import LanguageEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class EditLanguageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity | None) -> dict[str, str | int | bool | None] | None:
        if language is None:
            return None

        created_at = language.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = language.updated_at.strftime(cls.ACP_DATE_FORMAT) if language.updated_at else None

        return {
            'id': language.id,
            'code': language.code,
            'name': language.name,
            'is_active': language.is_active,
            'created_at': created_at,
            'updated_at': updated_at,
        }