from entities.Language.LanguageEntity import LanguageEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class AddPageTranslationLanguageTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, language: LanguageEntity | None) -> dict[str, str | int | bool | None] | None:
        if language is None:
            return None

        return {
            'id': language.id,
            'name': language.name,
        }