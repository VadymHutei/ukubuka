from vendor.ukubuka.repository import Repository
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
                `is_active`,
                `is_default`
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
                `name`,
                `is_active`,
                `is_default`
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

    def addText(self, text):
        query = '''
            INSERT INTO text (text)
            VALUES (%s)
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (text,))
                textID = cursor.lastrowid
            connection.commit()
        return textID

    def getTexts(self):
        query = '''
            SELECT
                text.id,
                text.text
            FROM text
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def setTranslations(self, textID, translations):
        query = '''
            INSERT INTO translation (text_id, language, translation)
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY UPDATE
                translation=translation
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                for language, translation in translations.items():
                    cursor.execute(query, (textID, language, translation))
            connection.commit()

    def getTranslations(self):
        query = '''
            SELECT
                translation.text_id,
                translation.language,
                translation.translation
            FROM translation
            JOIN language
                ON language.code = translation.language
                AND language.is_active = 1
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def getTranslationsForLanguage(self, language):
        query = '''
            SELECT
                text.id,
                text.text,
                translation.translation
            FROM text
            JOIN translation
                ON translation.text_id = text.id
            WHERE
                translation.language = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (language))
                result = cursor.fetchall()
        return result

    def getTextByID(self, textID):
        query = '''
            SELECT
                text.id,
                text.text
            FROM text
            WHERE
                text.id = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (textID,))
                return cursor.fetchone()

    def getTranslationsByTextID(self, textID):
        query = '''
            SELECT
                translation.language,
                translation.translation
            FROM translation
            WHERE
                translation.text_id = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (textID,))
                result = cursor.fetchall()
        return result

    def updateTranslations(self, data):
        query = '''
            INSERT INTO translation (
                text_id,
                language,
                translation
            )
            VALUES (%s, %s, %s)
            ON DUPLICATE KEY
            UPDATE
                translation = %s
        '''

        with self.getConnection() as connection:
            with connection.cursor() as cursor:
                for data in [(data['textID'], language, translation, translation) for language, translation in data['translations'].items()]:
                    cursor.execute(query, data)
                    print(cursor.rowcount)
            connection.commit()