from abc import ABC, abstractmethod

from entities.TextEntity import TextEntity


class ICodeTextRepository(ABC):

    @abstractmethod
    def find_translations_by_code(self, code: str) -> list[TextEntity]:
        pass