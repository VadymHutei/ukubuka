from flask import g, url_for

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from entities.Page.PageEntity import PageEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class PagesResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, page: PageEntity | None) -> dict[str, str | int | bool | None] | None:
        if page is None:
            return None

        info_page_url = url_for(
            ACP_PAGE_BLUEPRINT + '.page_route',
            language_code=g.current_language.code,
            page_id=page.id,
        )
        edit_page_url = url_for(
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
            'is_active': page.is_active,
            'info_page_url': info_page_url,
            'edit_page_url': edit_page_url,
            'delete_url': delete_url,
        }