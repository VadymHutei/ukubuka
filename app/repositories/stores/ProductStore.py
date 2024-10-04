from flask import g

from entities.Product.ProductEntity import ProductEntity
from repositories.stores.Store import Store


class ProductStore(Store[ProductEntity]):

    @staticmethod
    def key_for(product_id: int) -> str:
        return f'{product_id}_{g.current_language.code}'
