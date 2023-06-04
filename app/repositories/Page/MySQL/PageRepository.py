from flask import g
from entities.PageEntity import PageEntity
from repositories.Page.IPageRepository import IPageRepository
from repositories.MySQLRepository import MySQLRepository
from repositories.Page.MySQL.PageMapper import PageMapper


class PageRepository(IPageRepository, MySQLRepository):

    TABLE: str = 'page'

    def __init__(self, mapper: PageMapper) -> None:
        self._mapper = mapper

    def find_all(self):
        pass

    def find_by_code(self, code: str) -> PageEntity:
        query = f'''
            SELECT
                p.id,
                p.code,
                p.template,
                p.is_active,
                p.created_at,
                p.updated_at,
                pt.title
            FROM {self.TABLE} AS p
            JOIN {self.TABLE}_text AS pt
                ON pt.page_id = p.id
                AND pt.language_code = %s
            WHERE
                p.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (g.current_language.code, code))

        return self._mapper.from_row(cursor.fetchone())