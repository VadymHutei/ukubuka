from flask import current_app as app

from entities.Product.ProductEntity import ProductEntity
from repositories.Product.IProductDAO import IProductDAO
from repositories.Repository import Repository
from repositories.builders.Product.ProductBuilder import ProductBuilder
from repositories.builders.Product.ProductBuilderParams import ProductBuilderParams
from repositories.stores.Product.ProductStore import ProductStore


class ProductRepository(Repository):

    def __init__(self, product_dao: IProductDAO, product_store: ProductStore, product_builder: ProductBuilder):
        self._product_dao = product_dao
        self._product_store = product_store
        self._product_builder = product_builder

    def find(self, product_id: int, only_active: bool) -> ProductEntity | None:
        use_store = app.config['USE_ENTITY_STORE']
        store_key = ProductStore.key_for(product_id)

        if use_store and self._product_store.has(store_key):
            product = self._product_store.get(store_key)
            return None if only_active and not product.is_active else product

        product_builder_params = ProductBuilderParams(only_active=only_active)
        product = self._product_builder.build(product_id, product_builder_params)

        if product is None:
            return None

        if use_store:
            self._product_store.add(store_key, product)

        return None if only_active and not product.is_active else product

    def find_by_slug(self, slug: str, only_active: bool) -> ProductEntity | None:
        product_id = self._product_dao.find_id_by_slug(slug)

        if product_id is None:
            return None

        return self.find(product_id, only_active)
