from repositories.SQL.MySQL.Catalog.CatalogRepository import CatalogRepository
from repositories.SQL.MySQL.Config.ConfigRepository import ConfigRepository
from repositories.SQL.MySQL.Language.LanguageRepository import LanguageRepository
from repositories.SQL.MySQL.Page.PageRepository import PageRepository
from repositories.SQL.MySQL.Page.PageTextRepository import PageTextRepository
from repositories.builders.Product.IProductDAO import IProductDAO
from repositories.data_access.SQL.MySQL.ProductDAO import ProductDAO
from services.Catalog.ICatalogRepository import ICatalogRepository
from services.Config.IConfigRepository import IConfigRepository
from services.Language.ILanguageRepository import ILanguageRepository
from services.Page.IPageRepository import IPageRepository
from services.Page.IPageTextRepository import IPageTextRepository


services_map: dict[type, type] = {
    ICatalogRepository: CatalogRepository,
    IConfigRepository: ConfigRepository,
    ILanguageRepository: LanguageRepository,
    IPageRepository: PageRepository,
    IPageTextRepository: PageTextRepository,
    IProductDAO: ProductDAO,
}