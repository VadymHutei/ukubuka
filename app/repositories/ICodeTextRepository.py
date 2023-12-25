from abc import ABC, abstractmethod

from entities.TextEntity import TextEntity


class ICodeTextRepository(ABC):

    @abstractmethod
    def find_translations_by_entity_code(self, entity_code: str) -> list[TextEntity]:
        pass