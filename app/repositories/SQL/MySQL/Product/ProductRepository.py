from typing import Optional

from repositories.SQL.SQLRepository import SQLRepository
from repositories.SQL.MySQL.Product.mappers.ProductMapper import ProductMapper
from entities.Product.ProductEntity import ProductEntity
from services.Product.ProductRepository import ProductRepository


class ProductRepository(SQLRepository, ProductRepository):

    _TABLE = 'product'
    _MAPPER = ProductMapper

    def find_by_code(self, code: str) -> Optional[ProductEntity]:
        query = f'''
            SELECT
                {self._MAPPER.get_fields()}
            FROM {self._TABLE} AS p
            WHERE
                p.code = %s
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query, (code,))
                data = cursor.fetchone()

        return self._MAPPER.create_entity(data)