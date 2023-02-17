from entities.LanguageEntity import LanguageEntity
from repositories.Language.ILanguageRepository import ILanguageRepository
from repositories.MySQLRepository import MySQLRepository
from repositories.Language.MySQL.LanguageMapper import LanguageMapper


class LanguageRepository(ILanguageRepository, MySQLRepository):

    TABLE = 'language'

    def __init__(self, mapper: LanguageMapper) -> None:
        self._mapper = mapper

    def find_all(self) -> dict[str, LanguageEntity]:
        query = f'''
            SELECT
                code,
                name,
                is_active,
                is_default
            FROM
                {self.TABLE}
        '''
        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
        
        return self._mapper.from_rows(cursor.fetchall())