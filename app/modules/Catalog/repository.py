from flask import request

from config import DB_CREDENTIALS
from vendor.Ukubuka.repository import Repository


class CatalogRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)

    def getCatalogByAlias(self, catalogAlias):
        query = '''
            SELECT
                c.id,
                c.alias,
                ct.name
            FROM
                catalog AS c
            JOIN
                catalog_text AS ct ON ct.catalog_id = c.id
                AND ct.language = %s
            WHERE
                c.alias = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (request.ctx['language'], categoryAlias))
                result = cursor.fetchone()
        return result

    def getActiveProductsByCategoryAlias(self, categoryAlias):
        query = '''
            SELECT
                p.id,
                p.alias,
                p.price
            FROM category AS c
            JOIN
                product AS p ON p.category_id = c.id
            WHERE
                category.alias = %s
                AND p.is_active = 1
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, categoryAlias)
                result = cursor.fetchall()
        return result