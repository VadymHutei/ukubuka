from entities.Page.PageTextEntity import PageTextEntity
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class PageTextEntityTransformer(MySQLEntityTransformer):

    def __init__(self, mapper: PageTextMapper):
        super().__init__()

        self._mapper = mapper

    def transform(self, db_row: dict) -> PageTextEntity:
        return PageTextEntity(
            id=self._mapper.get_field_value_from_db_record(db_row, 'id'),
            page_id=self._mapper.get_field_value_from_db_record(db_row, 'page_id'),
            language_id=self._mapper.get_field_value_from_db_record(db_row, 'language_id'),
            title=self._mapper.get_field_value_from_db_record(db_row, 'title'),
            created_at=self._mapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=self._mapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )
