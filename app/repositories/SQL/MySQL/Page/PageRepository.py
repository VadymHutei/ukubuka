from flask import g

from entities.Page.PageEntity import PageEntity
from entities.Page.PageTextEntity import PageTextEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Page.IPageRepository import IPageRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageEntityTransformer import PageEntityTransformer
from transformers.entity_transformers.SQL.MySQL.Page.PageTextEntityTransformer import PageTextEntityTransformer


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

        query_data = (g.current_language.id, id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return PageEntityTransformer.transform(data) if data else None

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

        query_data = (g.current_language.id, code)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return PageEntityTransformer.transform(data) if data else None

    def find_all(self) -> list[PageEntity]:
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

        return PageEntityTransformer.transform_collection(data) if data else []

    def add(self, page: PageEntity) -> bool:
        query = f'''
            INSERT INTO {self.mapper.table} ({self.mapper.fillable_fields})
            VALUES ({self.mapper.fillable_placeholders()})
        '''

        query_data = PageMapper.fillable_data(page)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result

    def find_translations_by_code(self, code: str) -> list[PageTextEntity]:
        query = f'''
            SELECT
                {self.text_mapper.fields}
            FROM {self.text_mapper.table_as_prefix}
            JOIN {self.mapper.table_as_prefix}
                ON {self.mapper.field('id')} = {self.text_mapper.field('page_id')}
            WHERE
                {self.mapper.field('code')} = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return PageTextEntityTransformer.transform_collection(data) if data else [None]