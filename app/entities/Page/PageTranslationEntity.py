from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class PageTranslationEntity(Entity):

    page_id: int
    language_id: int
    title: str
    created_at: datetime

    id: int | None = None
    updated_at: datetime | None = None
