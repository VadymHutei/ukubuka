from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class LanguageEntityTransformer(MySQLEntityTransformer):

    def __init__(self, mapper: LanguageMapper):
        super().__init__()

        self._mapper = mapper

    def transform(self, db_row: dict) -> LanguageEntity:
        return LanguageEntity(
            id=self._mapper.get_field_value_from_db_record(db_row, 'id'),
            code=self._mapper.get_field_value_from_db_record(db_row, 'code'),
            name=self._mapper.get_field_value_from_db_record(db_row, 'name'),
            is_active=self._mapper.get_field_value_from_db_record(db_row, 'is_active'),
            created_at=self._mapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=self._mapper.get_field_value_from_db_record(db_row, 'updated_at'),
            deleted_at=self._mapper.get_field_value_from_db_record(db_row, 'deleted_at'),
        )
