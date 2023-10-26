from entities.Page.PageEntity import PageEntity
from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Page.PageRepositoryInterface import PageRepositoryInterface


class PageRepository(MySQLRepository, PageRepositoryInterface):

    def find_by_code(self, code: str) -> PageEntity | None:
        query = f'''
            SELECT
                {PageMapper.fields},
                {PageTextMapper.fields}
            FROM {PageMapper.table}
            JOIN {PageTextMapper.table}
                ON {PageTextMapper.table_prefix}.page_id = {PageMapper.table_prefix}.id
                AND {PageTextMapper.table_prefix}.language_id = %s
            WHERE
                {PageMapper.table_prefix}.code = %s
        '''

        query_data = (
            1,
            code,
        )

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)

        return PageMapper.create_entity(cursor.fetchone()) # type: ignore