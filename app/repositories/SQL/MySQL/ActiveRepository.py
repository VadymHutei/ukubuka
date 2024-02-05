from entities.Entity import Entity
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository


class ActiveRepository(MySQLRepository):

    def find_active(self) -> list[Entity]:
        query = f'''
            SELECT
                {self.mapper.fields}
            FROM {self.mapper.table_as_prefix}
            WHERE {self.mapper.pr_field('is_active')} = 1
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return self.transformer.transform_collection(data) if data else []