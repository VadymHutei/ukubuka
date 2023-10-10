from abc import ABC, abstractstaticmethod

from entities.IEntity import IEntity


class ResponseTransformer(ABC):

    @abstractstaticmethod
    def transform(entity: IEntity) -> dict[str, str|int]:
        pass

    @classmethod
    def collection(cls, entities: list[IEntity]) -> list[dict]:
        return [cls.transform(entity) for entity in entities]