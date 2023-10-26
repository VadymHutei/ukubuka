from dataclasses import dataclass
from datetime import datetime

from entities.IEntity import IEntity
from entities.Language.LanguageEntity import LanguageEntity


@dataclass
class PageTextEntity(IEntity):

    id: int
    page_id: int
    language_id: int
    title: str
    created_at: datetime
    updated_at: datetime | None = None

    language: LanguageEntity | None = None