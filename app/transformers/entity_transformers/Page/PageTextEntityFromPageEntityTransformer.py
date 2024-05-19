from datetime import datetime

from flask import g

from entities.Page.PageEntity import PageEntity
from entities.Page.PageTextEntity import PageTextEntity
from transformers.entity_transformers.EntityTransformer import EntityTransformer


class PageTextEntityFromPageEntityTransformer(EntityTransformer):

    def transform(self, page: PageEntity) -> PageTextEntity:
        return PageTextEntity(
            page_id=page.id,
            language_id=g.current_language.id,
            title=page.title,
            created_at=datetime.now(),
        )