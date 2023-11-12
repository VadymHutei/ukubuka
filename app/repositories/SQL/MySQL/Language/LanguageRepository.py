from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageRepository(MySQLRepository, ILanguageRepository):

    def find_all(self) -> list[LanguageEntity] | None:
        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table}
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
            FROM {LanguageMapper.table}
            WHERE {LanguageMapper.field('code')} = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (code,))
                data = cursor.fetchone()

        return LanguageMapper.create_entity(data) if data else None