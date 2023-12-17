from entities.Page.PageEntity import PageEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from transformers.entity_transformers.SQL.MySQL.MySQLEntityTransformer import MySQLEntityTransformer


class PageEntityTransformer(MySQLEntityTransformer):

    @classmethod
    def transform(cls, db_row: dict) -> PageEntity:
        return PageEntity(
            id=PageMapper.get_field_value_from_db_record(db_row, 'id'),
            code=PageMapper.get_field_value_from_db_record(db_row, 'code'),
            title=PageTextMapper.get_field_value_from_db_record(db_row, 'title'),
            template=PageMapper.get_field_value_from_db_record(db_row, 'template'),
            layout=PageMapper.get_field_value_from_db_record(db_row, 'layout'),
            is_active=PageMapper.get_field_value_from_db_record(db_row, 'is_active'),
            created_at=PageMapper.get_field_value_from_db_record(db_row, 'created_at'),
            updated_at=PageMapper.get_field_value_from_db_record(db_row, 'updated_at'),
        )