from flask import abort

from controllers.Controller import Controller
from services.Catalog.CatalogService import CatalogService
from views.HTML.website.Catalog.CatalogView import CatalogView


class CatalogController(Controller):

    def __init__(self, service: CatalogService) -> None:
        self._service = service

    def category_page_action(self, category_slug: str) -> str:
        category = self._service.find_category_by_slug(category_slug)

        if category is None:
            abort(404)

        category_products = self._service.find_category_products(category.code)

        view = CatalogView()
        view.set_data(
            category=category,
            products=category_products
        )

        return view.render()
