from dataclasses import dataclass

from entities.Entity import Entity


@dataclass
class ConfigEntity(Entity):

    code: str
    value: str
    created_at: str
    updated_at: str