from repositories.Product.IProductDAO import IProductDAO
from repositories.data_access.SQL.MySQL.MySQLDAO import MySQLDAO


class ProductDAO(IProductDAO, MySQLDAO):

    def find(self, product_id: int, only_active: bool) -> dict | None:
        query = f'''
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
                {'AND is_active = 1' if only_active else ''}
        '''

        query_data = (product_id,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                return cursor.fetchone()

    def find_id_by_slug(self, product_slug: str) -> int | None:
        query = f'SELECT id FROM product WHERE slug = %s'

        query_data = (product_slug,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return None if data is None else data['id']
