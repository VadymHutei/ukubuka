from flask import request
from modules.Base.repositories.MySQLRepository import MySQLRepository


class CatalogRepository(MySQLRepository):

    def getActiveCatalogs(self):
        query = '''
            SELECT
                c.id,
                c.alias,
                ct.name
            FROM
                catalog AS c
            JOIN
                catalog_text AS ct
                ON ct.catalog_id = c.id
                AND ct.language = %s
            WHERE
                c.is_active = 1
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (request.ctx['language'],))
                result = cursor.fetchall()
        return result

    def getCatalogByAlias(self, catalogAlias):
        query = '''
            SELECT
                c.id,
                c.alias,
                ct.name
            FROM
                catalog AS c
            JOIN
                catalog_text AS ct
                ON ct.catalog_id = c.id
                AND ct.language = %s
            WHERE
                c.alias = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (request.ctx['language'], catalogAlias))
                result = cursor.fetchone()
        return result

    def getCategoriesByCatalogID(self, catalogID):
        query = '''
            SELECT
                category_id AS id,
                filter
            FROM
                catalog_category
            WHERE
                catalog_id = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (catalogID,))
                result = cursor.fetchall()
        return result

    def getActiveProductsByCategoryAlias(self, categoryAlias):
        query = '''
            SELECT
                p.id,
                p.alias,
                p.price
            FROM
                category AS c
            JOIN
                product AS p
                ON p.category_id = c.id
            WHERE
                category.alias = %s
                AND p.is_active = 1
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (categoryAlias,))
                result = cursor.fetchall()
        return result

    def getProductsByCatalogID(self, catalogID):
        query = '''
            SELECT
                p.id,
                p.alias,
                p.category_id,
                p.price,
                p.is_active
            FROM
                catalog_product AS cp
            JOIN
                product AS p
                ON p.id = cp.product_id
            WHERE
                cp.catalog_id = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (catalogID,))
                result = cursor.fetchall()
        return result