from abc import ABC, abstractmethod

from entities.Catalog.CatalogEntity import CatalogEntity


class ICatalogRepository(ABC):

    @abstractmethod
    def get_all(self) -> list[CatalogEntity]:
        pass