from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity


@dataclass
class ConfigEntity(Entity):

    code: str
    value: str
    created_at: datetime

    updated_at: datetime | None = None
