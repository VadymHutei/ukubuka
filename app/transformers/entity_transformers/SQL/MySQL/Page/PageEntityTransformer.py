from entities.Page.PageEntity import PageEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class PageEntityTransformer(MySQLEntityTransformer):

    def __init__(self, mapper: PageMapper, text_mapper: PageTextMapper):
        super().__init__()

        self._mapper = mapper
        self._text_mapper = text_mapper

    def transform(self, db_row: dict) -> PageEntity:
        return PageEntity(
            id=self._mapper.get_field_value_from_db_record(db_row, 'id'),
            code=self._mapper.get_field_value_from_db_record(db_row, 'code'),
            title=self._text_mapper.get_field_value_from_db_record(db_row, 'title'),
            template=self._mapper.get_field_value_from_db_record(db_row, 'template'),
            layout=self._mapper.get_field_value_from_db_record(db_row, 'layout'),
            is_active=self._mapper.get_field_value_from_db_record(db_row, 'is_active'),
            created_at=self._mapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=self._mapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )
