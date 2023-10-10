from entities.Language.LanguageEntity import LanguageEntity
from response_transformers.web.WebResponseTransformer import WebResponseTransformer


class LanguageResponseTransformer(WebResponseTransformer):

    @staticmethod
    def transform(entity: LanguageEntity) -> dict[str, str|int]:
        return {
            'id': entity.id,
            'code': entity.code,
            'name': entity.name,
        }