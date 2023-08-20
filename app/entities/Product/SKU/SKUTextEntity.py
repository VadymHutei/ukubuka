from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from entities.Language.LanguageEntity import LanguageEntity


@dataclass
class SKUTextEntity(Entity):

    id: int
    sku_id: int
    language_id: int
    name: str
    description: str
    created_at: datetime
    updated_at: datetime|None

    language: LanguageEntity|None = None