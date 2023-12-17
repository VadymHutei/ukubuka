from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from entities.Page.PageEntity import PageEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class PagesResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, page: PageEntity | None) -> dict[str, str | int | bool | None] | None:
        if page is None:
            return None

        created_at = page.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = page.updated_at.strftime(cls.ACP_DATE_FORMAT) if page.updated_at else None

        info_page_url = url_for(
            ACP_PAGE_BLUEPRINT + '.page_route',
            language_code=g.current_language.code,
            code=page.code,
        )
        edit_page_url = url_for(
            ACP_PAGE_BLUEPRINT + '.edit_page_route',
            language_code=g.current_language.code,
            code=page.code,
        )
        delete_url = url_for(
            ACP_PAGE_BLUEPRINT + '.delete_page_route',
            language_code=g.current_language.code,
        )

        return {
            'id': page.id,
            'code': page.code,
            'title': page.title,
            'template': page.template,
            'layout': page.layout,
            'is_active': page.is_active,
            'created_at': created_at,
            'updated_at': updated_at,
            'info_page_url': info_page_url,
            'edit_page_url': edit_page_url,
            'delete_url': delete_url,
        }