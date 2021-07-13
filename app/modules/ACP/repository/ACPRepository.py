import pymysql.cursors

from config import DB_CREDENTIALS
from vendor.Ukubuka.repository import Repository


class ACPRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)
    
    def getCategories(self):
        query = f'''
            SELECT
                *
            FROM
                categories
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result