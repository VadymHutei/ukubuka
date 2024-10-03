from entities.Product.ProductEntity import ProductEntity
from repositories.Product.ProductRepository import ProductRepository
from services.IService import IService


class ProductService(IService):

    def __init__(self, repository: ProductRepository):
        self._repository = repository

    def find_by_slug(self, slug: str, only_active: bool = False) -> ProductEntity | None:
        return self._repository.find_by_slug(slug, only_active)
