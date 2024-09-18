from entities.Catalog.CatalogEntity import CatalogEntity
from services.Catalog.ICatalogRepository import ICatalogRepository
from services.IService import IService


class CatalogService(IService):

    def __init__(self, repository: ICatalogRepository) -> None:
        self._repository: ICatalogRepository = repository

    def find(self, catalog_id: int) -> CatalogEntity | None:
        return self._repository.find(catalog_id)

    def find_by_code(self, catalog_code: str) -> CatalogEntity | None:
        return self._repository.find_by_code(catalog_code)

    def find_all(self) -> list[CatalogEntity]:
        return self._repository.find_all()

    def find_category_by_code(self, category_code: str) -> CatalogEntity | None:
        pass