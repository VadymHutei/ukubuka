from controllers.IController import IController
from services.Catalog.CatalogService import CatalogService
from views.web.Catalog.CatalogView import CatalogView
from views.web.Catalog.CatalogsView import CatalogsView


class CatalogController(IController):

    def __init__(self, service: CatalogService) -> None:
        self._service: CatalogService = service

    def catalogs_page_action(self) -> str:
        view = CatalogsView()

        catalogs = self._service.get_all()

        view.set_data(catalogs=catalogs)

        return view.render()

    def catalog_page_action(self, catalog_code: str) -> str:
        view = CatalogView()

        catalog = self._service.find_by_code(catalog_code)

        view.set_data(catalog=catalog)

        return view.render()