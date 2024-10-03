from entities.Product.ProductEntity import ProductEntity
from repositories.Product.IProductDAO import IProductDAO
from repositories.builders.Product.ProductBuilder import ProductBuilder
from repositories.stores.ProductStore import ProductStore


class ProductRepository:

    def __init__(self, product_dao: IProductDAO, store: ProductStore, builder: ProductBuilder):
        self._product_dao = product_dao
        self._store = store
        self._builder = builder

    def find_by_slug(self, slug: str, only_active: bool = False) -> ProductEntity | None:
        product_id = self._product_dao.find_id_by_slug(slug, only_active)

        if product_id is None:
            return None

        if self._store.has(product_id):
            return self._store.get(product_id)
        else:
            product = self._builder.build(product_id)

            if product is not None:
                self._store.add(product)

            return product
