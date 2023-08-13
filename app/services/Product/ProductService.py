from services.Product.ProductRepository import ProductRepository
from entities.Product.ProductEntity import ProductEntity
from exceptions.ProductException import ProductException


class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository

    def get_by_code(self, code: str) -> ProductEntity:
        product = self.product_repository.find_by_code(code)

        if not product:
            raise ProductException('Product not found')

        return product