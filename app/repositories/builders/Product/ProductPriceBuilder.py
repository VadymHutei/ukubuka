from entities.Product.ProductPriceEntity import ProductPriceEntity
from repositories.Product.IProductPriceDAO import IProductPriceDAO
from repositories.builders.Builder import Builder
from repositories.builders.Product.ProductPriceBuilderParams import ProductPriceBuilderParams


class ProductPriceBuilder(Builder[ProductPriceEntity]):

    def __init__(
        self,
        product_price_dao: IProductPriceDAO,
    ):
        self._product_price_dao = product_price_dao

    def build(self, product_price_id: int, params: ProductPriceBuilderParams | None = None):
        product_price = self._create_price(product_price_id)

        if product_price is None:
            return None

        return product_price

    def _create_price(self, product_price_id: int):
        product_price_record = self._product_price_dao.find(product_price_id)

        if product_price_record is None:
            return None

        return ProductPriceEntity(
            id=product_price_record['id'],
            product_id=product_price_record['product_id'],
            currency_id=product_price_record['currency_id'],
            value=product_price_record['value'],
            created_at=product_price_record['created_at'],
            updated_at=product_price_record['updated_at'],
        )
