from abc import ABC, abstractmethod

from entities.Entity import Entity


class EntityMapper(ABC):

    @classmethod
    @abstractmethod
    def get_fields(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def get_table(cls) -> str:
        pass

    @classmethod
    @abstractmethod
    def create_entity(cls, db_record: dict) -> Entity:
        pass

    @classmethod
    @abstractmethod
    def create_entity_tuple(cls, db_records: list[dict]) -> tuple[Entity]:
        pass