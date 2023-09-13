from custom_types.Price import Price
from entities.Product.ProductEntity import ProductEntity
from transformers.response_transformers.Price.PriceTransformer import PriceTransformer
from transformers.Transformer import Transformer


class ProductTransformer(Transformer):

    @classmethod
    def transform(cls, product: ProductEntity) -> dict[str, str]:
        result = {
            'name': product.name,
            'description': product.description,
        }

        if product.price is not None and product.price.currency is not None:
            price = Price(product.price.value, product.price.currency)
            result['price'] = PriceTransformer.transform(price)

        return result