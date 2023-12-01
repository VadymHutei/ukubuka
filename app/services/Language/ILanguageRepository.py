from abc import abstractmethod

from entities.Language.LanguageEntity import LanguageEntity
from repositories.IRepository import IRepository
from value_objects.Language.LanguageVO import LanguageVO


class ILanguageRepository(IRepository):

    @abstractmethod
    def add(self, vo: LanguageVO) -> bool:
        pass

    def get_by_id(self, id: int) -> LanguageEntity:
        pass

    def get_by_code(self, code: str) -> LanguageEntity:
        pass

    @abstractmethod
    def find_all(self) -> list[LanguageEntity] | None:
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> LanguageEntity | None:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> LanguageEntity | None:
        pass

    @abstractmethod
    def update(self, entity: LanguageEntity) -> bool:
        pass

    @abstractmethod
    def delete_by_code(self, code: str) -> bool:
        pass

    @abstractmethod
    def get_only_active(self) -> list[LanguageEntity]:
        pass