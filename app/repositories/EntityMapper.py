from abc import ABC, abstractmethod

from entities.IEntity import IEntity


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
    def create_entity(cls, db_record: dict) -> IEntity:
        pass

    @classmethod
    @abstractmethod
    def create_entities(cls, db_records: list[dict]) -> list[IEntity]:
        pass