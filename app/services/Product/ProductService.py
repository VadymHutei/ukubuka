from entities.Product.ProductEntity import ProductEntity
from services.IService import IService
from services.Product.IProductRepository import IProductRepository


class ProductService(IService):

    def __init__(self, repository: IProductRepository):
        self._repository: IProductRepository = repository

    def find_by_slug(self, slug: str, only_active: bool = False) -> ProductEntity | None:
        return self._repository.find_by_slug(slug, only_active)
