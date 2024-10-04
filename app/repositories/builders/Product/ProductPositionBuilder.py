from flask import g

from entities.Product.ProductPositionEntity import ProductPositionEntity
from repositories.Product.IProductPositionDAO import IProductPositionDAO
from repositories.Product.IProductPositionTextDAO import IProductPositionTextDAO
from repositories.builders.Builder import Builder
from repositories.builders.Product.ProductPositionBuilderParams import ProductPositionBuilderParams


class ProductPositionBuilder(Builder[ProductPositionEntity]):

    def __init__(
        self,
        product_position_dao: IProductPositionDAO,
        product_position_text_dao: IProductPositionTextDAO,
    ):
        self._product_position_dao = product_position_dao
        self._product_position_text_dao = product_position_text_dao

    def build(self, product_position_id: int, params: ProductPositionBuilderParams):
        product_position = self._create_product_position(product_position_id, params.only_active)

        if product_position is None:
            return None

        self._build_text(product_position)

        return product_position

    def _create_product_position(self, product_position_id: int, only_active: bool) -> ProductPositionEntity | None:
        product_position_record = self._product_position_dao.find(product_position_id, only_active)

        if product_position_record is None:
            return None

        return ProductPositionEntity(
            id=product_position_record['id'],
            SKU=product_position_record['sku'],
            slug=product_position_record['slug'],
            product_id=product_position_record['product_id'],
            is_active=product_position_record['is_active'],
            created_at=product_position_record['created_at'],
            updated_at=product_position_record['updated_at'],
            deleted_at=product_position_record['deleted_at'],
        )

    def _build_text(self, product_position: ProductPositionEntity) -> None:
        product_position_text_record = self._product_position_text_dao.find_by_product_position_id_and_language_id(
            product_position.id,
            g.current_language.id,
        )

        if product_position_text_record is None:
            return None

        product_position.name = product_position_text_record['name']
        product_position.description = product_position_text_record['description']
