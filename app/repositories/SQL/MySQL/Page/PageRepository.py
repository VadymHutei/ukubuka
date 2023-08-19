from flask import g
from repositories.SQL.MySQL.Page.mappers.PageTextMapper import PageTextMapper

from repositories.SQL.SQLRepository import SQLRepository
from repositories.SQL.MySQL.Page.mappers.PageMapper import PageMapper
from services.Page.PageRepositoryInterface import PageRepositoryInterface
from entities.Page.PageEntity import PageEntity


class PageRepository(SQLRepository, PageRepositoryInterface):

    def find_by_code(self, code: str) -> PageEntity:
        query = f'''
            SELECT
                {PageMapper.get_fields()},
                {PageTextMapper.get_fields()}
            FROM {PageMapper.get_table()}
            JOIN {PageTextMapper.get_table()}
                ON {PageMapper.get_table_prefix()}.id = {PageTextMapper.get_table_prefix()}.page_id
                AND {PageTextMapper.get_table_prefix()}.language_id = %s
            WHERE
                p.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (g.current_language.code, code))

        return PageMapper.create_entity(cursor.fetchone())