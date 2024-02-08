from datetime import datetime
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository


class SoftDeleteRepository(MySQLRepository):

    def delete(self, entity_id: int) -> bool:
        query = f'''
            UPDATE {self.mapper.table_as_prefix}
            SET {self.mapper.pr_field('deleted_at')} = {SQLEntityMapper.QUERY_PLACEHOLDER}
            WHERE id = {SQLEntityMapper.QUERY_PLACEHOLDER}
        '''

        query_data = (datetime.now(), entity_id)

        with self.connection as connection:
            with connection.cursor() as cursor:
                result = cursor.execute(query, query_data) > 0

            connection.commit()
 
        return result