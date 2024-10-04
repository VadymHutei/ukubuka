from repositories.Product.IProductPositionDAO import IProductPositionDAO
from repositories.data_access.SQL.MySQL.MySQLDAO import MySQLDAO


class ProductPositionDAO(IProductPositionDAO, MySQLDAO):

    def find(self, product_position_id: int, only_active: bool) -> dict | None:
        query = f'''
            SELECT
                id,
                sku,
                slug,
                product_id,
                is_active,
                created_at,
                updated_at,
                deleted_at
            FROM
                product_position
            WHERE
                id = %s
                {'AND is_active = 1' if only_active else ''}
        '''

        query_data = (product_position_id,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                return cursor.fetchone()

    def find_ids_by_product_id(self, product_id: int, only_active: bool) -> list:
        query = f'''
            SELECT
                id
            FROM
                product_position
            WHERE
                product_id = %s
                {'AND is_active = 1' if only_active else ''}
        '''

        query_data = (product_id,)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchall()

        return [row['id'] for row in data]
