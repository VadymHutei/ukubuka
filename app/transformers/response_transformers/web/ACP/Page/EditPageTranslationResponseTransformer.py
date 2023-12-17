from entities.Page.PageTranslationEntity import PageTranslationEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class EditPageTranslationResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, translation: PageTranslationEntity | None) -> dict[str, str | int | bool | None] | None:
        if translation is None:
            return None

        return {
            'id': translation.id,
            'title': translation.title,
        }