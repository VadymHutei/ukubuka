from repositories.MySQLRepository import MySQLRepository


class LanguageRepository(MySQLRepository):

    TABLE = 'language'

    def find_all(self):
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
        
        return cursor.fetchall()