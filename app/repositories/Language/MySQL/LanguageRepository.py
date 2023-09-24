from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageRepository(MySQLRepository, ILanguageRepository):

    TABLE = 'language'

    def __init__(self, mapper: LanguageMapper) -> None:
        self._mapper = mapper

    def find_all(self) -> dict[str, LanguageEntity]:
        query = f'''
            SELECT
                code,
                name,
                is_active
            FROM
                {self.TABLE}
        '''
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
        
        return self._mapper.from_rows(cursor.fetchall())
    
    def find_by_code(self, code) -> LanguageEntity:
        query = f'''
            SELECT
                code,
                name,
                is_active
            FROM {self.TABLE}
            WHERE
                code = %s
        '''
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (code,))

        return self._mapper.from_row(cursor.fetchone())