from flask import g

from entities.Product.ProductEntity import ProductEntity
from repositories.Product.IProductDAO import IProductDAO
from repositories.Product.IProductTextDAO import IProductTextDAO
from repositories.builders.Builder import Builder


class ProductBuilder(Builder[ProductEntity]):

    def __init__(
        self,
        product_dao: IProductDAO,
        product_text_dao: IProductTextDAO,
    ):
        self._product_dao = product_dao
        self._product_text_dao = product_text_dao

    def build(self, product_id: int) -> ProductEntity | None:
        product = self._create_product(product_id)

        if product is None:
            return None

        self._build_text(product)

        return product

    def _create_product(self, product_id: int) -> ProductEntity | None:
        product_record = self._product_dao.find(product_id)

        if product_record is None:
            return None

        return ProductEntity(
            id=product_record['id'],
            slug=product_record['slug'],
            is_active=product_record['is_active'],
            created_at=product_record['created_at'],
            updated_at=product_record['updated_at'],
            deleted_at=product_record['deleted_at'],
        )

    def _build_text(self, product: ProductEntity) -> None:
        product_text_record = self._product_text_dao.find_by_product_id_and_language_id(
            product.id,
            g.current_language.id,
        )

        if product_text_record is None:
            return None

        product.name = product_text_record['name']
        product.description = product_text_record['description']
