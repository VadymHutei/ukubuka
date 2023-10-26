from entities.Language.LanguageEntity import LanguageEntity
from response_transformers.web.ACP.ACPWebResponseTransformer import ACPWebResponseTransformer


class EditLanguageResponseTransformer(ACPWebResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity) -> dict[str, str | int | bool]:
        created_at = language.created_at.strftime(cls.DATE_FORMAT)
        updated_at = language.updated_at.strftime(cls.DATE_FORMAT) if language.updated_at else '-'

        return {
            'id': language.id,
            'code': language.code,
            'name': language.name,
            'is_active': language.is_active,
            'created_at': created_at,
            'updated_at': updated_at,
        }