from abc import ABC, abstractmethod

from entities.Entity import Entity


class IActiveRepository(ABC):

    @abstractmethod
    def find_active(self) -> list[Entity]:
        pass