from entities.Page.PageTextEntity import PageTextEntity
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class PageTextEntityTransformer(MySQLEntityTransformer):

    @classmethod
    def transform(cls, db_row: dict) -> PageTextEntity:
        return PageTextEntity(
            id=PageTextMapper.get_field_value_from_db_record(db_row, 'id'),
            page_id=PageTextMapper.get_field_value_from_db_record(db_row, 'page_id'),
            language_id=PageTextMapper.get_field_value_from_db_record(db_row, 'language_id'),
            title=PageTextMapper.get_field_value_from_db_record(db_row, 'title'),
            created_at=PageTextMapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=PageTextMapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )