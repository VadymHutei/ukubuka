from entities.Product.ProductEntity import ProductEntity
from repositories.Product.ProductRepository import ProductRepository
from services.Service import Service


class ProductService(Service):

    def __init__(self, product_repository: ProductRepository):
        self._product_repository = product_repository

    def find_by_slug(self, slug: str, only_active: bool) -> ProductEntity | None:
        return self._product_repository.find_by_slug(slug, only_active)
