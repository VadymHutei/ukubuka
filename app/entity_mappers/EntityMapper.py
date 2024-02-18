from abc import ABC, abstractmethod
from typing import Type

from entities.Entity import Entity


class EntityMapper(ABC):

    _ENTITY_CLASS: Type[Entity]

    @classmethod
    @abstractmethod
    def create_entity(cls, data: dict) -> Entity:
        pass

    @classmethod
    @abstractmethod
    def create_entities(cls, data: list[dict]) -> list[Entity]:
        pass