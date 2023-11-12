from abc import abstractmethod

from entities.Language.LanguageEntity import LanguageEntity
from repositories.IRepository import IRepository


class ILanguageRepository(IRepository):

    @abstractmethod
    def find_all(self) -> list[LanguageEntity] | None:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> LanguageEntity | None:
        pass