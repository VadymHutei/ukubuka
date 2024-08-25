from controllers.IController import IController
from services.Catalog.CatalogService import CatalogService
from views.HTML.website.Catalog.CatalogsView import CatalogsView
from views.web.Catalog.CatalogView import CatalogView


class CatalogController(IController):

    def __init__(self, service: CatalogService) -> None:
        self._service: CatalogService = service

    def catalogs_page_action(self) -> str:
        view = CatalogsView()

        view.set_data(
            catalogs=self._service.find_all()
        )

        return view.render()

    def catalog_page_action(self, catalog_code: str) -> str:
        view = CatalogView()

        catalog = self._service.find_by_code(catalog_code)

        view.set_data(catalog=catalog)

        return view.render()