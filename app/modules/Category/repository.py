from flask import request

from config import DB_CREDENTIALS
from vendor.ukubuka.repository import Repository


class CategoryRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)

    def getAllSubcategories(self, categoryIDs):
        query = '''
            SELECT
                id,
                parent_id
            FROM
                category
            WHERE
                parent_id IS NOT NULL
                OR id IN (%s)
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (','.join(str(categoryID) for categoryID in categoryIDs),))
                result = cursor.fetchall()
        return result

    def getProductsByCategoryIDs(self, categoryIDs):
        query = '''
            SELECT
                p.id,
                p.alias,
                p.category_id,
                p.price,
                p.is_active,
                pt.name,
                pt.description
            FROM
                product AS p
            JOIN
                product_text AS pt
                ON pt.product_id = p.id
                AND pt.language = %s
            WHERE
                p.category_id IN (%s)
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (request.ctx['language'], ','.join(str(categoryID) for categoryID in categoryIDs),))
                result = cursor.fetchall()
        return result

    def getNumericCharacteristicsByProductIDs(self, productIDs):
        query = '''
            SELECT
                product_id,
                characteristic_id,
                value
            FROM
                product_characteristic_numeric
            WHERE
                product_id IN (%s)
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (','.join(str(productID) for productID in productIDs),))
                result = cursor.fetchall()
        return result

    def getTextCharacteristicsByProductIDs(self, productIDs):
        query = '''
            SELECT
                product_id,
                characteristic_id,
                value
            FROM
                product_characteristic_text
            WHERE
                language = %s
                AND product_id IN (%s)
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (request.ctx['language'], ','.join(str(productID) for productID in productIDs),))
                result = cursor.fetchall()
        return result