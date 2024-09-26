from entities.Product.ProductEntity import ProductEntity
from transformers.Transformer import Transformer


class ProductViewTransformer(Transformer):

    def transform(self, product: ProductEntity) -> dict:
        return {
            'name': product.name,
            'description': product.description,
        }
