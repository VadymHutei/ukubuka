from controllers.IController import IController
from services.Catalog.CatalogService import CatalogService


class CatalogController(IController):

    def __init__(self, service: CatalogService) -> None:
        self._service: CatalogService = service

    def getCatalogsPageAction(self):
        return 'catalogs'