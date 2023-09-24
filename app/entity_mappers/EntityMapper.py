from abc import ABC, abstractmethod
from typing import Self, Type

from entities.IEntity import IEntity
from value_objects.ValueObject import ValueObject


class EntityMapper(ABC):

    _ENTITY_CLASS: Type[IEntity|ValueObject]
    _NESTED_ENTITY_MAPPERS: dict[str, Type[Self]] = {}

    @classmethod
    @abstractmethod
    def create_entity(cls, data: dict) -> IEntity:
        pass

    @classmethod
    @abstractmethod
    def create_entities(cls, data: list[dict]) -> list[IEntity]:
        pass