from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from entities.Entity import Entity
from repositories.builders.BuilderParams import BuilderParams

T = TypeVar('T', bound=Entity)


class Builder(Generic[T], ABC):

    @abstractmethod
    def build(self, entity_id: int, params: BuilderParams | None = None) -> T | None:
        pass

    def build_collection(self, entity_ids: list[int], params: BuilderParams) -> dict[int, T]:
        result = {}

        for entity_id in entity_ids:
            entity = self.build(entity_id, params)

            if entity is not None:
                result[entity.id] = entity

        return result
