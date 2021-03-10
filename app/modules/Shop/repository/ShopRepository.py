import pymysql.cursors

from config import DB_CREDENTIALS
from ukubuka.AbstractRepository import AbstractRepository


class ShopRepository(AbstractRepository):
    
    def getCatalogByAlias(self, catalogAlias):
        query = f'''
            SELECT
                *
            FROM
                catalog
            WHERE
                alias = '{catalogAlias}'
        '''

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
        return result
    
    def getCatalogById(self, catalogID):
        query = f'''
            SELECT
                *
            FROM
                catalog
            WHERE
                id = '{catalogID}'
        '''

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
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

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
        return result
    
    def getCategoryByID(self, categoryID):
        query = f'''
            SELECT
                *
            FROM
                category
            WHERE
                id = '{alias}'
        '''

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
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

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
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

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
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

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
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

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
                print(result)
        return result