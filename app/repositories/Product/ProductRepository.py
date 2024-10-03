from flask import g

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

        if self._store.has(self._store_key(product_id)):
            return self._store.get(self._store_key(product_id))
        else:
            product = self._builder.build(product_id)

            if product is not None:
                self._store.add(self._store_key(product_id), product)

            return product

    def _store_key(self, product_id) -> str:
        return f'{product_id}_{g.current_language.code}'
