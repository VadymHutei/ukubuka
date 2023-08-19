from services.Language.ILanguageRepository import ILanguageRepository
from services.Product.ProductRepository import ProductRepository
from services.Page.PageRepository import PageRepository
from repositories.Language.MySQL.LanguageRepository import LanguageRepository
from repositories.SQL.MySQL.Product.ProductRepository import ProductRepository as MySQLProductRepository
from repositories.SQL.MySQL.Page.PageRepository import PageRepository as MySQLPageRepository


services_map: dict[type, type] = {
    ILanguageRepository: LanguageRepository,
    ProductRepository: MySQLProductRepository,
    PageRepository: MySQLPageRepository,
}