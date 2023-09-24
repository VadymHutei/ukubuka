from entities.Product.ProductEntity import ProductEntity
from entity_mappers.SQL.MySQL.Currency.CurrencyMapper import CurrencyMapper
from entity_mappers.SQL.MySQL.Product.ProductMapper import ProductMapper
from entity_mappers.SQL.MySQL.Product.ProductPriceMapper import ProductPriceMapper
from entity_mappers.SQL.MySQL.Product.ProductTextMapper import ProductTextMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Product.IProductRepository import IProductRepository


class ProductRepository(MySQLRepository, IProductRepository):

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

        return ProductMapper.create_entity(data) if data else None # type: ignore