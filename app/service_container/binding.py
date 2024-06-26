from repositories.SQL.MySQL.Catalog.CatalogRepository import CatalogRepository
from repositories.SQL.MySQL.Config.ConfigRepository import ConfigRepository
from repositories.SQL.MySQL.Language.LanguageRepository import LanguageRepository
from repositories.SQL.MySQL.Page.PageRepository import PageRepository
from repositories.SQL.MySQL.Page.PageTextRepository import PageTextRepository
from repositories.SQL.MySQL.Product.ProductRepository import ProductRepository
from services.Catalog.ICatalogRepository import ICatalogRepository
from services.Config.IConfigRepository import IConfigRepository
from services.Language.ILanguageRepository import ILanguageRepository
from services.Page.IPageRepository import IPageRepository
from services.Page.IPageTextRepository import IPageTextRepository
from services.Product.IProductRepository import IProductRepository


services_map: dict[type, type] = {
    ICatalogRepository: CatalogRepository,
    IConfigRepository: ConfigRepository,
    ILanguageRepository: LanguageRepository,
    IPageRepository: PageRepository,
    IPageTextRepository: PageTextRepository,
    IProductRepository: ProductRepository,
}