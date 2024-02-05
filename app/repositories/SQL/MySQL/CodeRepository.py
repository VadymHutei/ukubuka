from entities.Entity import Entity
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository


class CodeRepository(MySQLRepository):

    def find_by_code(self, code: str) -> Entity | None:
        query = f'''
            SELECT
                {self.mapper.fields}
            FROM {self.mapper.table_as_prefix}
            WHERE
                {self.mapper.pr_field('code')} = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return self.transformer.transform(data) if data else None

    def delete_by_code(self, code: str) -> bool:
        query = f'DELETE FROM {self.mapper.table} WHERE code = {SQLEntityMapper.QUERY_PLACEHOLDER}'

        query_data = (code,)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()

        return result