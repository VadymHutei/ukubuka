from entities.Config.ConfigEntity import ConfigEntity
from entity_mappers.SQL.MySQL.Config.ConfigMapper import ConfigMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Config.ConfigRepositoryInterface import IConfigRepository


class ConfigRepository(MySQLRepository, IConfigRepository):

    def get_all(self) -> list[ConfigEntity]:
        query = f'''
            SELECT
                {ConfigMapper.fields}
            FROM {ConfigMapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return ConfigMapper.create_entities(data) if data else None # type: ignore

    def get_config(self) -> list[ConfigEntity]:
        query = f'''
            SELECT
                {ConfigMapper.fields}
            FROM {ConfigMapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return ConfigMapper.create_entities(data) if data else () # type: ignore