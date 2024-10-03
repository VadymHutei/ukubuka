from repositories.builders.Product.IProductDAO import IProductDAO
from repositories.data_access.SQL.MySQL.MySQLDAO import MySQLDAO


class ProductDAO(IProductDAO, MySQLDAO):

    def find(self, product_id: int) -> dict | None:
        query = '''
            SELECT
                id,
                slug,
                is_active,
                created_at,
                updated_at,
                deleted_at
            FROM
                product
            WHERE
                id = %s
        '''

        query_data = (product_id,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return data

    def find_id_by_slug(self, product_slug: str, only_active: bool = False) -> int | None:
        only_active_condition = 'AND is_active = 1' if only_active else ''
        query = f'SELECT id FROM product WHERE slug = %s {only_active_condition}'

        query_data = (product_slug,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return None if data is None else data['id']
