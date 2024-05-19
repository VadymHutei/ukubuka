from abc import ABC, abstractmethod

from entities.Language.LanguageEntity import LanguageEntity
from repositories.Repository import Repository


class ILanguageRepository(Repository, ABC):

    @abstractmethod
    def find(self, language_id: int) -> LanguageEntity | None:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> LanguageEntity | None:
        pass

    @abstractmethod
    def find_all(self) -> list[LanguageEntity]:
        pass

    @abstractmethod
    def find_active(self) -> list[LanguageEntity]:
        pass

    @abstractmethod
    def add(self, entity: LanguageEntity) -> int | None:
        pass

    @abstractmethod
    def update(self, entity: LanguageEntity) -> bool:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> bool:
        pass
