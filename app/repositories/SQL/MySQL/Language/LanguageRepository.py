from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageRepository(MySQLRepository, ILanguageRepository):

    def get_all(self, with_inactive: bool = False) -> list[LanguageEntity]:
        conditions = []

        if not with_inactive:
            conditions.append('is_active = 1')

        query = f'''
            SELECT
                {LanguageMapper.fields}
            FROM {LanguageMapper.table}
            {self.create_where_conditions(conditions)}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return LanguageMapper.create_entities(data) if data else None # type: ignore