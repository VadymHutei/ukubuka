from controllers.IController import IController
from services.Product.ProductService import ProductService
from views.web.Product.ProductView import ProductView


class ProductController(IController):

    def __init__(self, service: ProductService):
        self._service = service

    def product_page_action(self, code: str) -> str:
        product = self._service.find_by_code(code)

        view = ProductView()
        view.set_data(product=product)

        return view.render()