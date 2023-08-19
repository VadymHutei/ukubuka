from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from entities.Entity import Entity
from entities.Language.LanguageEntity import LanguageEntity


@dataclass
class ProductTextEntity(Entity):

    id: int
    product_id: int
    language_id: int
    name: str
    description: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    language: Optional[LanguageEntity] = None