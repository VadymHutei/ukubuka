from entities.Catalog.CatalogEntity import CatalogEntity
from entity_mappers.SQL.MySQL.Catalog.CatalogMapper import CatalogMapper
from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Catalog.ICatalogRepository import ICatalogRepository


class CatalogRepository(MySQLRepository, ICatalogRepository):

    def get_all(self) -> list[CatalogEntity]:
        query = f'''
            SELECT
                {CatalogMapper.fields}
            FROM {CatalogMapper.table}
        '''

        with self.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                data = cursor.fetchall()

        return CatalogMapper.create_entities(data) if data else None # type: ignore