from dataclasses import dataclass

from entities.IEntity import IEntity


@dataclass
class ConfigEntity(IEntity):

    id: int
    code: str
    value: str
    created_at: str
    updated_at: str