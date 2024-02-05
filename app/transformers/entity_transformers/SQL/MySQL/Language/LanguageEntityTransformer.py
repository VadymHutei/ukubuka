from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class LanguageEntityTransformer(MySQLEntityTransformer):

    @classmethod
    def transform(cls, db_row: dict) -> LanguageEntity:
        return LanguageEntity(
            id=LanguageMapper.get_field_value_from_db_record(db_row, 'id'),
            code=LanguageMapper.get_field_value_from_db_record(db_row, 'code'),
            name=LanguageMapper.get_field_value_from_db_record(db_row, 'name'),
            is_active=LanguageMapper.get_field_value_from_db_record(db_row, 'is_active'),
            created_at=LanguageMapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=LanguageMapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )