from typing import TypeVar, Generic

from entities.Entity import Entity

T = TypeVar('T', bound=Entity)


# TODO: Redis
class Store(Generic[T]):

    def __init__(self):
        self._entities = {}

    def has(self, entity_id: int) -> bool:
        return entity_id in self._entities

    def get(self, entity_id: int) -> T:
        return self._entities[entity_id]

    def find(self, entity_id: int) -> T | None:
        return self._entities.get(entity_id, None)

    def add(self, entity: T) -> None:
        self._entities[entity.id] = entity
