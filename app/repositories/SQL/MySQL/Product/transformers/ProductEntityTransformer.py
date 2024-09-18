from entities.Product.ProductEntity import ProductEntity
from repositories.SQL.MySQL.Product.mappers.ProductMapper import ProductMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class ProductEntityTransformer(MySQLEntityTransformer):

    def __init__(self, mapper: ProductMapper, text_mapper: ProductTextMapper):
        super().__init__()

        self._mapper = mapper
        self._text_mapper = text_mapper

    def transform(self, db_row: dict) -> ProductEntity:
        return ProductEntity(
            id=self._mapper.get_field_value_from_db_record(db_row, 'id'),
            slug=self._mapper.get_field_value_from_db_record(db_row, 'slug'),
            name=self._text_mapper.get_field_value_from_db_record(db_row, 'name'),
            description=self._text_mapper.get_field_value_from_db_record(db_row, 'description'),
            is_active=self._mapper.get_field_value_from_db_record(db_row, 'is_active'),
            created_at=self._mapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=self._mapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )
