from flask import g

from entities.Page.PageEntity import PageEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Page.IPageRepository import IPageRepository


class PageRepository(MySQLRepository, IPageRepository):

    def find_by_code(self, code: str) -> PageEntity | None:
        query = f'''
            SELECT
                {PageMapper.fields},
                {PageTextMapper.fields}
            FROM {PageMapper.table_as_prefix}
            JOIN {PageTextMapper.table_as_prefix}
                ON {PageTextMapper.table_prefix}.page_id = {PageMapper.table_prefix}.id
                AND {PageTextMapper.table_prefix}.language_id = %s
            WHERE
                {PageMapper.table_prefix}.code = %s
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
                {PageMapper.fields},
                {PageTextMapper.fields}
            FROM {PageMapper.table_as_prefix}
            JOIN {PageTextMapper.table_as_prefix}
                ON {PageTextMapper.field('page_id')} = {PageMapper.field('id')}
                AND {PageTextMapper.field('language_id')} = %s
        '''

        query_data = (g.current_language.id,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return PageMapper.create_entities(data) if data else []