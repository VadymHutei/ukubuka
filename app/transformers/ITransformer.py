from abc import ABC, abstractmethod

from entities.IEntity import IEntity


class ITransformer(ABC):

    @classmethod
    @abstractmethod
    def transform(cls, entity: IEntity | None) -> dict[str, str | int | bool | None] | None:
        pass

    @classmethod
    def transform_collection(cls, entities: list[IEntity] | None) -> list[dict[str, str | int | bool | None]] | None:
        if entities is None:
            return None

        return [cls.transform(entity) for entity in entities]