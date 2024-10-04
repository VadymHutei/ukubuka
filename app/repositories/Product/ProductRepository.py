from entities.Product.ProductEntity import ProductEntity
from repositories.Product.IProductDAO import IProductDAO
from repositories.builders.Product.ProductBuilder import ProductBuilder
from repositories.stores.ProductStore import ProductStore


class ProductRepository:

    def __init__(self, product_dao: IProductDAO, store: ProductStore, builder: ProductBuilder):
        self._product_dao = product_dao
        self._store = store
        self._builder = builder

    def find(self, product_id: int, only_active: bool = False) -> ProductEntity | None:
        if self._store.has(ProductStore.key_for(product_id)):
            product = self._store.get(ProductStore.key_for(product_id))
        else:
            product = self._builder.build(product_id)

            if product is not None:
                self._store.add(ProductStore.key_for(product_id), product)

        if only_active and not product.is_active:
            return None

        return product

    def find_by_slug(self, slug: str, only_active: bool = False) -> ProductEntity | None:
        product_id = self._product_dao.find_id_by_slug(slug)

        if product_id is None:
            return None

        return self.find(product_id, only_active)
