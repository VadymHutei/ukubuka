from entities.Catalog.CatalogEntity import CatalogEntity
from services.Catalog.ICatalogRepository import ICatalogRepository
from services.IService import IService


class CatalogService(IService):

    def __init__(self, repository: ICatalogRepository) -> None:
        self._repository: ICatalogRepository = repository

    def get_all(self) -> list[CatalogEntity]:
        return self._repository.get_all()

    def find_by_code(self, code: str) -> CatalogEntity | None:
        return self._repository.find_by_code(code)