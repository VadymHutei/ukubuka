from flask import abort

from controllers.IController import IController
from services.Catalog.CatalogService import CatalogService
from views.HTML.website.Catalog.CatalogView import CatalogView
from views.HTML.website.Catalog.CatalogsView import CatalogsView


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

        if catalog is None:
            abort(404)

        view.set_data(
            catalog=self._service.find_by_code(catalog_code)
        )

        return view.render()
