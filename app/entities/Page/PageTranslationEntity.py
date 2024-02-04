from dataclasses import dataclass
from datetime import datetime

from entities.TextEntity import TextEntity


@dataclass
class PageTranslationEntity(TextEntity):

    page_id: int
    language_id: int
    title: str
    created_at: datetime

    updated_at: datetime | None = None