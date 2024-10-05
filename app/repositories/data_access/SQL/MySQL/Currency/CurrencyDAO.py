from repositories.Currency.ICurrencyDAO import ICurrencyDAO
from repositories.data_access.SQL.MySQL.MySQLDAO import MySQLDAO


class CurrencyDAO(ICurrencyDAO, MySQLDAO):

    def find(self, currency_id: int, only_active: bool):
        query = f'''
            SELECT
                id,
                code,
                symbol,
                symbol_position,
                is_active,
                created_at,
                updated_at
            FROM
                currency
            WHERE
                id = %s
                {'AND is_active = 1' if only_active else ''}
        '''

        query_data = (currency_id,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                return cursor.fetchone()

    def find_by_code(self, currency_code: str, only_active: bool):
        query = f'''
            SELECT
                id,
                code,
                symbol,
                symbol_position,
                is_active,
                created_at,
                updated_at
            FROM
                currency
            WHERE
                code = %s
                {'AND is_active = 1' if only_active else ''}
        '''

        query_data = (currency_code,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                return cursor.fetchone()

    def find_id_by_code(self, currency_code: str):
        query = f'SELECT id FROM currency WHERE code = %s'

        query_data = (currency_code,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return None if data is None else data['id']