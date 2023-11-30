from abc import ABC, abstractmethod
from typing import Self, Type

from entities.Entity import Entity
from value_objects.IValueObject import IValueObject


class EntityMapper(ABC):

    _ENTITY_CLASS: Type[Entity | IValueObject]
    _NESTED_ENTITY_MAPPERS: dict[str, Type[Self]] = {}

    @classmethod
    @abstractmethod
    def create_entity(cls, data: dict) -> Entity:
        pass

    @classmethod
    @abstractmethod
    def create_entities(cls, data: list[dict]) -> list[Entity]:
        pass