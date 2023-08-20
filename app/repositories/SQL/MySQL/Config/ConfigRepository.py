from entities.Config.ConfigEntity import ConfigEntity
from repositories.SQL.MySQL.Config.ConfigMapper import ConfigMapper
from repositories.SQL.SQLRepository import SQLRepository
from services.Config.ConfigRepositoryInterface import ConfigRepositoryInterface


class ConfigRepository(SQLRepository, ConfigRepositoryInterface):

    def get_config(self) -> list[ConfigEntity]:
        query = f'''
            SELECT
                {ConfigMapper.fields}
            FROM {ConfigMapper.table}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return ConfigMapper.create_entity_tuple(data) if data else ()