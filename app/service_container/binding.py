from services.Language.LanguageRepositoryInterface import LanguageRepositoryInterface
from services.Product.ProductRepositoryInterface import ProductRepositoryInterface
from services.Page.PageRepositoryInterface import PageRepositoryInterface
from repositories.SQL.MySQL.Language.LanguageRepository import LanguageRepository as MySQLLanguageRepository
from repositories.SQL.MySQL.Product.ProductRepository import ProductRepository as MySQLProductRepository
from repositories.SQL.MySQL.Page.PageRepository import PageRepository as MySQLPageRepository


services_map: dict[type, type] = {
    LanguageRepositoryInterface: MySQLLanguageRepository,
    ProductRepositoryInterface: MySQLProductRepository,
    PageRepositoryInterface: MySQLPageRepository,
}