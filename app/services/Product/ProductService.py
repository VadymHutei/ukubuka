from entities.Product.ProductEntity import ProductEntity
from exceptions.entities_exceptions.ProductException import ProductException
from services.Product.ProductRepositoryInterface import ProductRepositoryInterface
from services.Service import Service


class ProductService(Service):

    def __init__(self, product_repository: ProductRepositoryInterface):
        self.product_repository = product_repository

    def get_by_code(self, code: str) -> ProductEntity:
        product = self.product_repository.find_by_code(code)

        if not product:
            raise ProductException('Product not found')

        return product

    def find_by_code(self, code: str) -> ProductEntity|None:
        return self.product_repository.find_by_code(code)