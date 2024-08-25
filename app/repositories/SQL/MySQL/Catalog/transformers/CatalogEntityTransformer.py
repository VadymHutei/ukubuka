from entities.Catalog.CatalogEntity import CatalogEntity
from repositories.SQL.MySQL.Catalog.mappers.CatalogMapper import CatalogMapper
from repositories.SQL.MySQL.Catalog.mappers.CatalogTextMapper import CatalogTextMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class CatalogEntityTransformer(MySQLEntityTransformer):

    def __init__(self, mapper: CatalogMapper, text_mapper: CatalogTextMapper):
        super().__init__()

        self._mapper = mapper
        self._text_mapper = text_mapper

    def transform(self, db_row: dict) -> CatalogEntity:
        return CatalogEntity(
            id=self._mapper.get_field_value_from_db_record(db_row, 'id'),
            code=self._mapper.get_field_value_from_db_record(db_row, 'code'),
            name=self._text_mapper.get_field_value_from_db_record(db_row, 'name'),
            description=self._text_mapper.get_field_value_from_db_record(db_row, 'description'),
            is_active=self._mapper.get_field_value_from_db_record(db_row, 'is_active'),
            created_at=self._mapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=self._mapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )
