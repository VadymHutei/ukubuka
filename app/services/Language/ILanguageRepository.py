from abc import abstractmethod

from entities.Language.LanguageEntity import LanguageEntity
from repositories.IRepository import IRepository


class ILanguageRepository(IRepository):

    @abstractmethod
    def get_all(self, with_inactive: bool = False) -> list[LanguageEntity]:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> LanguageEntity | None:
        pass