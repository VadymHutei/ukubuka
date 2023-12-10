from flask import g

from entities.Page.PageEntity import PageEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Page.IPageRepository import IPageRepository
from value_objects.Page.PageVO import PageVO


class PageRepository(MySQLRepository, IPageRepository):

    mapper = PageMapper
    text_mapper = PageTextMapper

    def find_by_id(self, id: int) -> PageEntity | None:
        query = f'''
            SELECT
                {self.mapper.fields},
                {self.text_mapper.fields}
            FROM {self.mapper.table_as_prefix}
            LEFT JOIN {self.text_mapper.table_as_prefix}
                ON {self.text_mapper.table_prefix}.page_id = {self.mapper.table_prefix}.id
                AND {self.text_mapper.table_prefix}.language_id = %s
            WHERE
                {self.mapper.table_prefix}.id = %s
        '''

        query_data = (1, id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return PageMapper.create_entity(data) if data else None

    def find_by_code(self, code: str) -> PageEntity | None:
        query = f'''
            SELECT
                {self.mapper.fields},
                {self.text_mapper.fields}
            FROM {self.mapper.table_as_prefix}
            LEFT JOIN {self.text_mapper.table_as_prefix}
                ON {self.text_mapper.table_prefix}.page_id = {self.mapper.table_prefix}.id
                AND {self.text_mapper.table_prefix}.language_id = %s
            WHERE
                {self.mapper.table_prefix}.code = %s
        '''

        query_data = (1, code)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return PageMapper.create_entity(data) if data else None

    def get_all(self) -> list[PageEntity]:
        query = f'''
            SELECT
                {self.mapper.fields},
                {self.text_mapper.fields}
            FROM {self.mapper.table_as_prefix}
            LEFT JOIN {self.text_mapper.table_as_prefix}
                ON {self.text_mapper.field('page_id')} = {self.mapper.field('id')}
                AND {self.text_mapper.field('language_id')} = %s
        '''

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return PageMapper.create_entities(data) if data else []

    def add(self, vo: PageVO) -> bool:
        query = f'INSERT INTO {self.mapper.table} ({self.mapper.fillable}) VALUES ({self.mapper.fillable_placeholders()})'

        query_data = PageMapper.fillable_data(vo)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result