from typing import Optional

from entities.Page.PageEntity import PageEntity
from services.Page.PageRepositoryInterface import PageRepositoryInterface
from repositories.SQL.MySQL.Page.mappers.PageTextMapper import PageTextMapper
from repositories.SQL.SQLRepository import SQLRepository
from repositories.SQL.MySQL.Page.mappers.PageMapper import PageMapper


class PageRepository(SQLRepository, PageRepositoryInterface):

    def find_by_code(self, code: str) -> Optional[PageEntity]:
        query = f'''
            SELECT
                {PageMapper.fields},
                {PageTextMapper.fields}
            FROM {PageMapper.table}
            JOIN {PageTextMapper.table}
                ON {PageMapper.table_prefix}.id = {PageTextMapper.table_prefix}.page_id
                AND {PageTextMapper.table_prefix}.language_id = %s
            WHERE
                {PageMapper.table_prefix}.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (1, code))

        return PageMapper.create_entity(cursor.fetchone())