from repositories.Product.IProductPositionTextDAO import IProductPositionTextDAO
from repositories.data_access.SQL.MySQL.MySQLDAO import MySQLDAO


class ProductPositionTextDAO(IProductPositionTextDAO, MySQLDAO):

    def find_by_product_position_id_and_language_id(self, product_position_id: int, language_id: int) -> dict | None:
        query = '''
            SELECT
                id,
                product_position_id,
                language_id,
                name,
                description,
                created_at,
                updated_at
            FROM
                product_position_text
            WHERE
                product_position_id = %s
                AND language_id = %s
        '''

        query_data = (product_position_id, language_id)

        with self._connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, query_data)
                data = cursor.fetchone()

        return data
