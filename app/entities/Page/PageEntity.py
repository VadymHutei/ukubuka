from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class PageEntity(Entity):

    code: str
    template: str
    is_active: bool
    title: str
    created_at: datetime

    layout: str | None = None
    updated_at: datetime | None = None
