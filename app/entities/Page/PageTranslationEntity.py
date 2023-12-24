from dataclasses import dataclass
from datetime import datetime

from entities.TextEntity import TextEntity


@dataclass
class PageTranslationEntity(TextEntity):

    language_id: int
    page_id: int
    title: str
    created_at: datetime

    updated_at: datetime | None = None