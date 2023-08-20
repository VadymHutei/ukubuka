from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from entities.Language.LanguageEntity import LanguageEntity


@dataclass
class PageTextEntity(Entity):

    id: int
    page_id: int
    language_id: int
    title: str
    created_at: datetime
    updated_at: datetime|None

    language: LanguageEntity|None = None