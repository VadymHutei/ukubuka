from abc import abstractmethod

from entities.Catalog.CatalogEntity import CatalogEntity
from repositories.IRepository import IRepository


class ICatalogRepository(IRepository):

    @abstractmethod
    def get_all(self) -> list[CatalogEntity]:
        pass