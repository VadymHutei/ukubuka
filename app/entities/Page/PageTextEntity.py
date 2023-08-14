from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from entities.Entity import Entity

@dataclass
class PageTextEntity(Entity):

    id: int
    page_id: int
    language_id: int
    title: str
    created_at: datetime
    updated_at: Optional[datetime] = None