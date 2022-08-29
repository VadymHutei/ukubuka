from typing import Optional, Union

from modules.Base.repositories.MySQLRepository import MySQLRepository
from modules.Language.entities.LanguageEntity import LanguageEntity


class LanguageRepository(MySQLRepository):

    @classmethod
    def create_language_entity(cls, row: Optional[dict]) -> Union[LanguageEntity, None]:
        if row is None:
            return None

        return LanguageEntity(
            code=row['code'],
            name=row['name'],
            is_active=bool(row['is_active']),
            is_default=bool(row['is_default']),
        )

    def get_languages(self) -> list[LanguageEntity]:
        query = '''
            SELECT
                code,
                name,
                is_active,
                is_default
            FROM
                language
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return [LanguageRepository.create_language_entity(row) for row in cursor.fetchall()]

    def get_default_language(self) -> Union[LanguageEntity, None]:
        query = '''
            SELECT
                code,
                name,
                is_active,
                is_default
            FROM
                language
            WHERE
                is_default = 1 AND
                is_active = 1
            LIMIT 1
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return LanguageRepository.create_language_entity(cursor.fetchone())

    def addText(self, text):
        query = '''
            INSERT INTO text (text)
            VALUES (%s)
        '''

        with self.get_connection() as connection:
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

        with self.get_connection() as connection:
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

        with self.get_connection() as connection:
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
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return cursor.fetchall()

    def getTextByID(self, textID):
        query = '''
            SELECT
                text.id,
                text.text
            FROM text
            WHERE
                text.id = %s
        '''

        with self.get_connection() as connection:
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

        with self.get_connection() as connection:
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

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                for data in [(data['textID'], language, translation, translation) for language, translation in data['translations'].items()]:
                    cursor.execute(query, data)
            connection.commit()

    def deleteTranslations(self, textID):
        query = '''
            DELETE FROM translation
            WHERE
                text_id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (textID,))
            connection.commit()

    def deleteText(self, textID):
        query = '''
            DELETE FROM text
            WHERE
                id = %s
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (textID,))
            connection.commit()
