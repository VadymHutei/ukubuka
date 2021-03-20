import pymysql.cursors

from config import DB_CREDENTIALS
from ukubuka.AbstractRepository import AbstractRepository


class ACPRepository(AbstractRepository):
    
    def getCategories(self):
        query = f'''
            SELECT
                *
            FROM
                categories
        '''

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result