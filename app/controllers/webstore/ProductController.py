from flask import abort

from controllers.IController import IController
from services.Product.ProductService import ProductService
from views.web.Product.ProductView import ProductView


class ProductController(IController):

    def __init__(self, service: ProductService) -> None:
        self._service = service

    def product_page_action(self, product_slug: str) -> str:
        product = self._service.find_by_slug(product_slug, True)

        if product is None:
            abort(404)

        view = ProductView()
        view.set_data(product=product)

        return view.render()
