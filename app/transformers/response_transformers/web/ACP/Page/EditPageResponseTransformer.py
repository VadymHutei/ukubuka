from entities.Page.PageEntity import PageEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class EditPageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, page: PageEntity | None) -> dict[str, str | int | bool | None] | None:
        if page is None:
            return None

        return {
            'id': page.id,
            'code': page.code,
            'template': page.template,
            'layout': page.layout,
            'is_active': page.is_active,
        }