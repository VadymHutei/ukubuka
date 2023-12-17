from entities.Page.PageTextEntity import PageTextEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class PageTextResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, page_text: PageTextEntity | None) -> dict[str, str | int | bool | None] | None:
        if page_text is None:
            return None

        created_at = page_text.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = page_text.updated_at.strftime(cls.ACP_DATE_FORMAT) if page_text.updated_at else None

        return {
            'id': page_text.id,
            'title': page_text.title,
            'page_id': page_text.page_id,
            'language_id': page_text.language_id,
            'created_at': created_at,
            'updated_at': updated_at,
        }