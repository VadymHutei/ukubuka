from typing import Union

from modules.Base.repositories.MySQLRepository import MySQLRepository
from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.entities.TextEntity import TextEntity


class LanguageRepository(MySQLRepository):

    @classmethod
    def create_language_entity(cls, data: dict) -> Union[LanguageEntity, None]:
        return LanguageEntity(
            code=data['code'],
            name=data['name'],
            is_active=bool(data['is_active']),
            is_default=bool(data['is_default']),
        )

    @classmethod
    def create_text_entity(cls, data: dict) -> Union[TextEntity, None]:
        return TextEntity(
            ID=int(data['id']),
            text=data['text'],
        )

    def get_languages(self, only_active: bool = False) -> dict[str, LanguageEntity]:
        only_active_condition = 'WHERE is_active = 1' if only_active else ''
        query = f'''
            SELECT
                code,
                name,
                is_active,
                is_default
            FROM
                language
            {only_active_condition}
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                return {row['code']: LanguageRepository.create_language_entity(row) for row in cursor.fetchall()}

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

    def get_texts(self) -> dict[int, TextEntity]:
        get_texts_query = '''
            SELECT
                id,
                text
            FROM
                text
        '''
        get_translations_query = '''
            SELECT
                text_id,
                language,
                translation
            FROM
                translation
        '''

        with self.get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(get_texts_query)
                texts_data = cursor.fetchall()
                cursor.execute(get_translations_query)
                translations_data = cursor.fetchall()

        texts = {int(text_row['id']): LanguageRepository.create_text_entity(text_row) for text_row in texts_data}

        for translation_row in translations_data:
            text_ID = int(translation_row['text_id'])

            if text_ID not in texts:
                continue

            texts[text_ID].translations[translation_row['language']] = translation_row['translation']

        return texts

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
