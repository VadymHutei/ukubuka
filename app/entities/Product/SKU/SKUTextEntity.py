from dataclasses import dataclass
from typing import Optional

from entities.Entity import Entity
from entities.Language.LanguageEntity import LanguageEntity


@dataclass
class SKUTextEntity(Entity):

    id: int
    sku_id: int
    language_id: int
    name: str
    description: str
    created_at: str
    updated_at: str

    language: Optional[LanguageEntity] = None