from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Catalog.ICatalogRepository import ICatalogRepository


class CatalogRepository(MySQLRepository, ICatalogRepository):
    pass