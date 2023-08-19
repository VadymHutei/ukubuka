from services.Service import Service
from services.Product.ProductRepositoryInterface import ProductRepositoryInterface
from entities.Product.ProductEntity import ProductEntity
from exceptions.entities_exception.ProductException import ProductException


class ProductService(Service):

    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def get_by_code(self, code: str) -> ProductEntity:
        product = self.product_repository.find_by_code(code)

        if not product:
            raise ProductException('Product not found')

        return product