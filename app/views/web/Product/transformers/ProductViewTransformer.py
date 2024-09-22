from entities.Product.ProductEntity import ProductEntity
from transformers.Transformer import Transformer


class ProductViewTransformer(Transformer):

    @classmethod
    def transform(cls, product: ProductEntity) -> dict:
        return {
            'name': product.name,
            'description': product.description,
        }
