from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from entities.Page.PageEntity import PageEntity
from transformers.response_transformers.web.ACP.ACPWebResponseTransformer import WebACPResponseTransformer


class PageResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, page: PageEntity | None) -> dict[str, str | int | bool | None] | None:
        if page is None:
            return None

        created_at = page.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = page.updated_at.strftime(cls.ACP_DATE_FORMAT) if page.updated_at else None

        add_translation_url = url_for(
            ACP_PAGE_BLUEPRINT + '.add_page_translation_route',
            language_code=g.current_language.code,
            page_id=page.id,
        )
        edit_url = url_for(
            ACP_PAGE_BLUEPRINT + '.edit_page_route',
            language_code=g.current_language.code,
            page_id=page.id,
        )
        delete_url = url_for(
            ACP_PAGE_BLUEPRINT + '.delete_page_route',
            language_code=g.current_language.code,
            page_id=page.id,
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
            'add_translation_url': add_translation_url,
            'edit_url': edit_url,
            'delete_url': delete_url,
        }