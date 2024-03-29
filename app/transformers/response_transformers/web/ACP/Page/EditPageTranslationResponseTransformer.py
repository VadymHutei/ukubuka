from entities.Page.PageTextEntity import PageTextEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class EditPageTranslationResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, translation: PageTextEntity | None) -> dict[str, str | int | bool | None] | None:
        if translation is None:
            return None

        return {
            'id': translation.id,
            'title': translation.title,
        }