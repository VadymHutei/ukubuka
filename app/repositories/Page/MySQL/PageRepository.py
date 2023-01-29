from flask import g
from entities.Page import Page
from repositories.Page.IPageRepository import IPageRepository
from repositories.MySQLRepository import MySQLRepository
from repositories.Page.MySQL.PageMapper import PageMapper


class PageRepository(IPageRepository, MySQLRepository):

    TABLE: str = 'page'

    def __init__(self, mapper: PageMapper) -> None:
        self._mapper = mapper

    def find_all(self):
        pass

    def find_by_code(self, code: str) -> Page:
        query = f'''
            SELECT
                page.id,
                page.code,
                page.template,
                page.is_active,
                page.created_at,
                page.updated_at,
                text.title
            FROM {self.TABLE} AS page
            JOIN {self.TABLE}_text AS text
                ON text.page_id = page.id
                AND text.language_code = %s
            WHERE
                page.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (g.current_language.code, code))

        return self._mapper.from_row(cursor.fetchone())