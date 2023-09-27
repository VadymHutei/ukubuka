from abc import abstractmethod

from entities.Catalog.CatalogEntity import CatalogEntity
from repositories.IRepository import IRepository


class ICatalogRepository(IRepository):

    @abstractmethod
    def get_all(self) -> list[CatalogEntity]:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> CatalogEntity|None:
        pass