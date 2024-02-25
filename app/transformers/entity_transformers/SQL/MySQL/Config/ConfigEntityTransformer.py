from entities.Config.ConfigEntity import ConfigEntity
from entity_mappers.SQL.MySQL.Config.ConfigMapper import ConfigMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class ConfigEntityTransformer(MySQLEntityTransformer):

    def __init__(self, mapper: ConfigMapper):
        super().__init__()

        self._mapper = mapper

    def transform(self, db_row: dict) -> ConfigEntity:
        return ConfigEntity(
            id=self._mapper.get_field_value_from_db_record(db_row, 'id'),
            code=self._mapper.get_field_value_from_db_record(db_row, 'code'),
            value=self._mapper.get_field_value_from_db_record(db_row, 'value'),
            created_at=self._mapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=self._mapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )
