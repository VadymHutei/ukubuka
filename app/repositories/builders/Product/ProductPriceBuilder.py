from entities.Product.ProductPriceEntity import ProductPriceEntity
from repositories.Product.IProductPriceDAO import IProductPriceDAO
from repositories.builders.Builder import Builder
from repositories.builders.Currency.CurrencyBuilder import CurrencyBuilder
from repositories.builders.Currency.CurrencyBuilderParams import CurrencyBuilderParams
from repositories.builders.Product.ProductPriceBuilderParams import ProductPriceBuilderParams


class ProductPriceBuilder(Builder[ProductPriceEntity]):

    def __init__(
        self,
        product_price_dao: IProductPriceDAO,
        currency_builder: CurrencyBuilder,
    ):
        self._product_price_dao = product_price_dao
        self._currency_builder = currency_builder

    def build(self, product_price_id: int, params: ProductPriceBuilderParams | None = None):
        product_price = self._create_price(product_price_id)

        if product_price is None:
            return None

        self._build_currency(product_price)

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

    def _build_currency(self, product_price: ProductPriceEntity):
        currency_builder_params = CurrencyBuilderParams(only_active=False)
        currency = self._currency_builder.build(product_price.currency_id, currency_builder_params)

        if currency is None:
            return

        product_price.currency = currency
