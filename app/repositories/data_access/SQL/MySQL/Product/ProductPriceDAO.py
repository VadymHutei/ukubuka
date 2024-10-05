from repositories.Product.IProductPriceDAO import IProductPriceDAO
from repositories.data_access.SQL.MySQL.MySQLDAO import MySQLDAO


class ProductPriceDAO(IProductPriceDAO, MySQLDAO):

    def find(self, product_price_id: int):
        query = f'''
            SELECT
                id,
                product_id,
                currency_id,
                value,
                created_at,
                updated_at
            FROM
                product_price
            WHERE
                id = %s
        '''

        query_data = (product_price_id,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                return cursor.fetchone()

    def find_by_product_id_and_currency_id(self, product_id: int, currency_id: int):
        query = f'''
            SELECT
                id,
                product_id,
                currency_id,
                value,
                created_at,
                updated_at
            FROM
                product_price
            WHERE
                product_id = %s
                AND currency_id = %s
        '''

        query_data = (product_id, currency_id)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                return cursor.fetchone()

    def find_id_by_product_id_and_currency_id(self, product_id: int, currency_id: int):
        query = f'SELECT id FROM product_price WHERE product_id = %s AND currency_id = %s'

        query_data = (product_id, currency_id)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return None if data is None else data['id']
