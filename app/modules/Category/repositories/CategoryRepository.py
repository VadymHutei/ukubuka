from flask import request

from modules.Base.Repository import Repository


class CategoryRepository(Repository):

    def getCategories(self):
        query = '''
            SELECT
                category.id,
                category.alias,
                category.parent_id,
                category.created_datetime,
                category.changed_datetime,
                category.is_active,
                category_text.name
            FROM
                category
            LEFT JOIN category_text
                ON category_text.category_id = category.id
                AND category_text.language = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (request.ctx['language'].code))
                result = cursor.fetchall()
        return result

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