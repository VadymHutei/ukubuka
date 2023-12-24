from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class PageEntity(Entity):

    code: str
    template: str
    is_active: bool
    created_at: datetime

    title: str | None = None
    layout: str | None = None
    updated_at: datetime | None = None