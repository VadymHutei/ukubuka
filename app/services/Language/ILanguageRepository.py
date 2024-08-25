from abc import ABC, abstractmethod

from entities.Language.LanguageEntity import LanguageEntity
from repositories.IRepository import IRepository


class ILanguageRepository(IRepository, ABC):

    @abstractmethod
    def find_by_code(self, code: str) -> LanguageEntity | None:
        pass

    @abstractmethod
    def find_active(self) -> list[LanguageEntity]:
        pass
