from datetime import datetime

from entities.Entity import Entity


class LanguageEntity(Entity):

    id: int
    code: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None