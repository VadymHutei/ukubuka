from entities.Config.ConfigEntity import ConfigEntity
from entity_mappers.SQL.MySQL.Config.ConfigMapper import ConfigMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Config.ConfigRepositoryInterface import IConfigRepository
from transformers.entity_transformers.SQL.MySQL.Config.ConfigEntityTransformer import ConfigEntityTransformer


class ConfigRepository(MySQLRepository, IConfigRepository):

    def __init__(self, mapper: ConfigMapper):
        super().__init__()

        self._mapper = mapper
        self._transformer = ConfigEntityTransformer

    def get_all(self) -> list[ConfigEntity]:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM {self._mapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return self._transformer.transform(data) if data else None

    def get_config(self) -> list[ConfigEntity]:
        query = f'''
            SELECT
                {self._mapper.fields}
            FROM {self._mapper.table_as_prefix}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return self._transformer.transform_collection(data) if data else []
