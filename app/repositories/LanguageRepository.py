from entities.Language import Language
from repositories.MySQLRepository import MySQLRepository
from repositories.mappers.LanguageMapper import LanguageMapper


class LanguageRepository(MySQLRepository):

    TABLE = 'language'

    def __init__(self, mapper: LanguageMapper) -> None:
        self._mapper = mapper

    def find_all(self) -> dict[str, Language]:
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