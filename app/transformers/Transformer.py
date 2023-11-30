from abc import ABC, abstractmethod

from entities.Entity import Entity


class Transformer(ABC):

    @classmethod
    @abstractmethod
    def transform(cls, entity: Entity | None) -> dict[str, str | int | bool | None] | None:
        pass

    @classmethod
    def transform_collection(cls, entities: list[Entity] | None) -> list[dict[str, str | int | bool | None]] | None:
        if entities is None:
            return None

        return [cls.transform(entity) for entity in entities]