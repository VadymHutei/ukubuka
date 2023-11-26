from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository
from value_objects.Language.LanguageVO import LanguageVO


class LanguageRepository(MySQLRepository, ILanguageRepository):

    def add(self, language_vo: LanguageVO) -> bool:
        placeholders = ', '.join(['%s'] * LanguageMapper.fillable_length)

        query = f'INSERT INTO {LanguageMapper.table} ({LanguageMapper.fillable}) VALUES ({placeholders})'

        query_data = LanguageMapper.fillable_data(language_vo)

        with self.connection as connection:
            with connection.cursor() as cursor:
                return cursor.execute(query, query_data) > 0

    def find_all(self) -> list[LanguageEntity] | None:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return LanguageMapper.create_entities(data) if data else None

    def find_by_code(self, code: str) -> LanguageEntity | None:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table_as_prefix}
            WHERE {LanguageMapper.field('code')} = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (code,))
                data = cursor.fetchone()

        return LanguageMapper.create_entity(data) if data else None