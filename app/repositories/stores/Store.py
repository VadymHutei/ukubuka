from typing import TypeVar, Generic

from entities.Entity import Entity

T = TypeVar('T', bound=Entity)


# TODO: Redis
class Store(Generic[T]):

    def __init__(self):
        self._entities = {}

    def has(self, key: str) -> bool:
        return key in self._entities

    def get(self, key: str) -> T:
        return self._entities[key]

    def find(self, key: str) -> T | None:
        return self._entities.get(key, None)

    def add(self, key: str, entity: T) -> None:
        self._entities[key] = entity
