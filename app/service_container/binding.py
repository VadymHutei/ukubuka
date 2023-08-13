from repositories.SQL.MySQL.Product.ProductRepository import ProductRepository as MySQLProductRepository
from services.Language.ILanguageRepository import ILanguageRepository
from repositories.Language.MySQL.LanguageRepository import LanguageRepository
from services.Product.ProductRepository import ProductRepository


services_map: dict[type, type] = {
    ILanguageRepository: LanguageRepository,
    ProductRepository: MySQLProductRepository
}