import pymysql.cursors

from config import DB_CREDENTIALS
from ukubuka.AbstractRepository import AbstractRepository


class LanguageRepository(AbstractRepository):

    def getLanguages(self):
        query = '''
            SELECT
                `code`,
                `name`,
                `is_active`
            FROM
                `language`
        '''

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result

    def getDefaultLanguage(self):
        query = '''
            SELECT
                `code`,
                `name`
            FROM
                `language`
            WHERE
                `is_default` = 1 AND
                `is_active` = 1
            LIMIT 1
        '''

        connection = pymysql.connect(**DB_CREDENTIALS)
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result