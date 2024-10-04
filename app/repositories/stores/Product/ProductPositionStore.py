from flask import g

from entities.Product.ProductPositionEntity import ProductPositionEntity
from repositories.stores.Store import Store


class ProductPositionStore(Store[ProductPositionEntity]):

    @staticmethod
    def key_for(product_position_id: int) -> str:
        return f'{product_position_id}_{g.current_language.code}'
