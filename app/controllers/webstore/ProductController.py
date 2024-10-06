from flask import abort

from controllers.Controller import Controller
from service_container import sc
from services.Product.ProductService import ProductService
from views.web.Product.ProductView import ProductView


class ProductController(Controller):

    def __init__(self, product_service: ProductService) -> None:
        self._product_service = product_service

    def product_page_action(self, product_slug: str) -> str:
        product = self._product_service.find_by_slug(product_slug, only_active=True)

        if product is None:
            abort(404)

        view = sc.get(ProductView)
        view.set_data(product=product)

        return view.render()
