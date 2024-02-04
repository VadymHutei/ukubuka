from flask import url_for, g

from blueprints.blueprint_names import ACP_PAGE_BLUEPRINT
from entities.Page.PageTranslationEntity import PageTranslationEntity
from transformers.response_transformers.web.ACP.WebACPResponseTransformer import WebACPResponseTransformer


class PageTranslationResponseTransformer(WebACPResponseTransformer):

    @classmethod
    def transform(cls, translation: PageTranslationEntity | None) -> dict[str, str | int | bool | None] | None:
        if translation is None:
            return None

        created_at = translation.created_at.strftime(cls.ACP_DATE_FORMAT)
        updated_at = translation.updated_at.strftime(cls.ACP_DATE_FORMAT) if translation.updated_at else None

        edit_url = url_for(
            ACP_PAGE_BLUEPRINT + '.edit_page_translation_route',
            language_code=g.current_language.code,
            translation_id=translation.id,
        )

        return {
            'id': translation.id,
            'page_id': translation.page_id,
            'language_id': translation.language_id,
            'title': translation.title,
            'created_at': created_at,
            'updated_at': updated_at,
            'edit_url': edit_url,
        }