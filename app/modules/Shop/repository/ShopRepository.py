import pymysql.cursors

from config import DB_CREDENTIALS
from vendor.Ukubuka.repository import Repository


class ShopRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)
    
    def getCatalogByAlias(self, catalogAlias):
        query = f'''
            SELECT
                *
            FROM
                catalog
            WHERE
                alias = '{catalogAlias}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result
    
    def getCatalogByID(self, catalogID):
        query = f'''
            SELECT
                *
            FROM
                catalog
            WHERE
                id = '{catalogID}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result
    
    def getCategoryByAlias(self, categoryAlias):
        query = f'''
            SELECT
                *
            FROM
                category
            WHERE
                alias = '{categoryAlias}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result
    
    def getCategoryByID(self, categoryID):
        query = f'''
            SELECT
                *
            FROM
                category
            WHERE
                id = '{categoryID}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result

    def getProductsByCategoryID(self, categoryID):
        query = f'''
            SELECT
                *
            FROM
                product
            WHERE
                category_id = {categoryID}
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result
    
    def getProductByAlias(self, productAlias):
        query = f'''
            SELECT
                *
            FROM
                product
            WHERE
                alias = '{productAlias}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result
    
    def getProductByID(self, productID):
        query = f'''
            SELECT
                *
            FROM
                product
            WHERE
                alias = '{productID}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result
    
    def getSKUByAlias(self, SKUAlias):
        query = f'''
            SELECT
                *
            FROM
                sku
            WHERE
                alias = '{SKUAlias}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result
    
    def getSKUByID(self, SKUID):
        query = f'''
            SELECT
                *
            FROM
                sku
            WHERE
                alias = '{SKUID}'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result