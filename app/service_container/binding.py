from repositories.SQL.MySQL.Catalog.CatalogRepository import CatalogRepository
from repositories.SQL.MySQL.Config.ConfigRepository import ConfigRepository as MySQLConfigRepository
from repositories.SQL.MySQL.Language.LanguageRepository import LanguageRepository as MySQLLanguageRepository
from repositories.SQL.MySQL.Page.PageRepository import PageRepository as MySQLPageRepository
from repositories.SQL.MySQL.Product.ProductRepository import ProductRepository as MySQLProductRepository
from services.Catalog.ICatalogRepository import ICatalogRepository
from services.Config.ConfigRepositoryInterface import IConfigRepository
from services.Language.LanguageRepositoryInterface import LanguageRepositoryInterface
from services.Page.PageRepositoryInterface import PageRepositoryInterface
from services.Product.ProductRepositoryInterface import ProductRepositoryInterface


services_map: dict[type, type] = {
    LanguageRepositoryInterface: MySQLLanguageRepository,
    ProductRepositoryInterface: MySQLProductRepository,
    PageRepositoryInterface: MySQLPageRepository,
    IConfigRepository: MySQLConfigRepository,
    ICatalogRepository: CatalogRepository,
}