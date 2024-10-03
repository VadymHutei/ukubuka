from entities.Product.ProductEntity import ProductEntity
from repositories.builders.Builder import Builder
from repositories.builders.Product.IProductDAO import IProductDAO


class ProductBuilder(Builder[ProductEntity]):

    def __init__(self, dao: IProductDAO):
        self._dao = dao

    def build(self, product_id: int) -> ProductEntity | None:
        product = self._create_product(product_id)

        if product is None:
            return None

        return product

    def _create_product(self, product_id: int) -> ProductEntity | None:
        product_record = self._dao.find(product_id)

        if product_record is None:
            return None

        return ProductEntity(
            product_record['id'],
            product_record['slug'],
            product_record['is_active'],
            product_record['created_at'],
            product_record['updated_at'],
            product_record['deleted_at'],
        )
