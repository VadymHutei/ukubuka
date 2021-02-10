from modules.Catalog.controller import CatalogController
from modules.Catalog.service import CatalogService
from modules.Catalog.view import CatalogView


class CatalogProvider:

    @staticmethod
    def getResources():
        return {
            CatalogController: (CatalogService, CatalogView),
            CatalogService: (),
            CatalogView: ('catalog/page.html',)
        }