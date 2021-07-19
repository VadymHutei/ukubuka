from vendor.Ukubuka.repository import Repository
from config import DB_CREDENTIALS


class LanguageRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)

    def getLanguages(self):
        query = '''
            SELECT
                `code`,
                `name`,
                `is_active`
            FROM
                `language`
        '''
        with self.getConnection() as connection:
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
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchone()
        return result

    def getTranslations(self):
        query = '''
            SELECT
                t.`text`,
                t.`language`,
                t.`translation`
            FROM
                `translation` AS t
            JOIN `language` AS l
                ON l.`code` = t.`language`
            WHERE l.`is_active` = 1
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
        return result

    def getTranslationsForLanguage(self, language):
        query = '''
            SELECT
                t.`text`,
                t.`language`,
                t.`translation`
            FROM
                `translation` AS t
            JOIN `language` AS l
                ON l.`code` = t.`language`
            WHERE l.`code` = %s'
        '''
        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (language))
                result = cursor.fetchall()
        return result

    def addTranslation(self, language, text, translation):
        query = '''
            INSERT INTO `translation` (`text`, `language`, `translation`)
            VALUES (%s, %s, %s)
        '''
        params = (text, language, translation)

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, params)
            connection.commit()