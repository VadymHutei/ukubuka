from flask import current_app as app
from flask import g

from entities.Product.ProductEntity import ProductEntity
from repositories.Product.IProductDAO import IProductDAO
from repositories.Product.IProductPositionDAO import IProductPositionDAO
from repositories.Product.IProductTextDAO import IProductTextDAO
from repositories.builders.Builder import Builder
from repositories.builders.Product.ProductBuilderParams import ProductBuilderParams
from repositories.builders.Product.ProductPositionBuilder import ProductPositionBuilder
from repositories.builders.Product.ProductPositionBuilderParams import ProductPositionBuilderParams
from repositories.stores.Product.ProductPositionStore import ProductPositionStore


class ProductBuilder(Builder[ProductEntity]):

    def __init__(
        self,
        product_dao: IProductDAO,
        product_text_dao: IProductTextDAO,
        product_position_dao: IProductPositionDAO,
        product_position_builder: ProductPositionBuilder,
        product_position_store: ProductPositionStore,
    ):
        self._product_dao = product_dao
        self._product_text_dao = product_text_dao
        self._product_position_dao = product_position_dao
        self._product_position_builder = product_position_builder
        self._product_position_store = product_position_store

    def build(self, product_id: int, params: ProductBuilderParams):
        product = self._create_product(product_id, params.only_active)

        if product is None:
            return None

        self._build_text(product)
        self._build_positions(product, params.only_active)

        return product

    def _create_product(self, product_id: int, only_active: bool) -> ProductEntity | None:
        product_record = self._product_dao.find(product_id, only_active)

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

    def _build_positions(self, product: ProductEntity, only_active: bool) -> None:
        product_position_ids = self._product_position_dao.find_ids_by_product_id(product.id, only_active)
        use_store = app.config['USE_ENTITY_STORE']

        for product_position_id in product_position_ids:
            store_key = ProductPositionStore.key_for(product_position_id)

            if use_store and self._product_position_store.has(store_key):
                product_position = self._product_position_store.get(store_key)
            else:
                builder_params = ProductPositionBuilderParams(only_active=True)
                product_position = self._product_position_builder.build(product_position_id, builder_params)

                if use_store and product_position is not None:
                    self._product_position_store.add(store_key, product_position)

            if product_position is None or (only_active and not product_position.is_active):
                continue

            product.positions[product_position.id] = product_position
