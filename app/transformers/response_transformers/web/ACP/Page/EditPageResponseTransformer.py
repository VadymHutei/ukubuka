from entities.Page.PageEntity import PageEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class EditPageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, page: PageEntity | None) -> dict[str, str | int | bool | None] | None:
        if page is None:
            return None

        created_at = page.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = page.updated_at.strftime(cls.ACP_DATE_FORMAT) if page.updated_at else None

        return {
            'id': page.id,
            'code': page.code,
            'template': page.template,
            'layout': page.layout,
            'is_active': page.is_active,
            'created_at': created_at,
            'updated_at': updated_at,
        }