from entities.Product.ProductEntity import ProductEntity
from repositories.SQL.MySQL.Currency.CurrencyMapper import CurrencyMapper
from repositories.SQL.MySQL.Product.mappers.ProductMapper import ProductMapper
from repositories.SQL.MySQL.Product.mappers.ProductPriceMapper import ProductPriceMapper
from repositories.SQL.MySQL.Product.mappers.ProductTextMapper import ProductTextMapper
from repositories.SQL.SQLRepository import SQLRepository
from services.Product.ProductRepositoryInterface import ProductRepositoryInterface


class ProductRepository(SQLRepository, ProductRepositoryInterface):

    def find_by_code(self, code: str) -> ProductEntity|None:
        query = f'''
            SELECT
                {ProductMapper.fields},
                {ProductTextMapper.fields},
                {ProductPriceMapper.fields},
                {CurrencyMapper.fields}
            FROM {ProductMapper.table}
            JOIN {ProductTextMapper.table}
                ON {ProductTextMapper.table_prefix}.product_id = {ProductMapper.table_prefix}.id
                AND {ProductTextMapper.table_prefix}.language_id = %s
            JOIN {ProductPriceMapper.table}
                ON {ProductPriceMapper.table_prefix}.product_id = {ProductMapper.table_prefix}.id
            LEFT JOIN {CurrencyMapper.table}
                ON {CurrencyMapper.table_prefix}.id = {ProductPriceMapper.table_prefix}.currency_id
                AND {CurrencyMapper.table_prefix}.is_active = 1
            WHERE
                {ProductMapper.table_prefix}.code = %s
            LIMIT 1
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                # cursor.execute(query, (g.current_language.id, code))
                cursor.execute(query, (1, code))
                data = cursor.fetchone()

        return ProductMapper.create_entity(data) if data else None