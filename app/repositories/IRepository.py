from abc import ABC, abstractmethod

from entities.Entity import Entity


class IRepository(ABC):

    @abstractmethod
    def find(self, entity_id: int) -> Entity | None:
        pass

    @abstractmethod
    def find_all(self) -> list[Entity]:
        pass

    @abstractmethod
    def add(self, entity: Entity) -> bool:
        pass

    @abstractmethod
    def update(self, entity: Entity) -> bool:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        pass