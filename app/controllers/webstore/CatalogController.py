from controllers.IController import IController
from services.Catalog.CatalogService import CatalogService


class CatalogController(IController):

    def __init__(self, service: CatalogService) -> None:
        self._service: CatalogService = service

    def get_catalogs_page_action(self):
        catalogs = self._service.get_all()
        print(catalogs)

        return 'catalogs'

    def get_catalog_page_action(self, catalog_code: str):
        return f'catalog {catalog_code}'