from controllers.Controller import Controller
from services.Product.ProductService import ProductService
from views.web.ProductView import ProductView


class ProductController(Controller):

    def __init__(self, product_service: ProductService):
        super().__init__()

        self.product_service = product_service

    def product_page_action(self, code: str) -> str:
        product = self.product_service.get_by_code(code)

        view = ProductView()
        view.set_data(product=product)

        return view.render()