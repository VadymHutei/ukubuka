from entities.Product.ProductEntity import ProductEntity
from services.Price.ProductPriceService import ProductPriceService
from transformers.Transformer import Transformer


class ProductViewTransformer(Transformer):

    def __init__(self, price_service: ProductPriceService):
        self._price_service = price_service

    def transform(self, product: ProductEntity) -> dict:
        return {
            'name': product.name,
            'description': product.description,
            'price': self._price_service.format(product.price),
        }
