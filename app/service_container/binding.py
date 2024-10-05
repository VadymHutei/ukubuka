from repositories.Currency.ICurrencyDAO import ICurrencyDAO
from repositories.Product.IProductDAO import IProductDAO
from repositories.Product.IProductPositionDAO import IProductPositionDAO
from repositories.Product.IProductPositionTextDAO import IProductPositionTextDAO
from repositories.Product.IProductPriceDAO import IProductPriceDAO
from repositories.Product.IProductTextDAO import IProductTextDAO
from repositories.SQL.MySQL.Catalog.CatalogRepository import CatalogRepository
from repositories.SQL.MySQL.Config.ConfigRepository import ConfigRepository
from repositories.SQL.MySQL.Language.LanguageRepository import LanguageRepository
from repositories.SQL.MySQL.Page.PageRepository import PageRepository
from repositories.SQL.MySQL.Page.PageTextRepository import PageTextRepository
from repositories.data_access.SQL.MySQL.Currency.CurrencyDAO import CurrencyDAO
from repositories.data_access.SQL.MySQL.Product.ProductDAO import ProductDAO
from repositories.data_access.SQL.MySQL.Product.ProductPositionDAO import ProductPositionDAO
from repositories.data_access.SQL.MySQL.Product.ProductPositionTextDAO import ProductPositionTextDAO
from repositories.data_access.SQL.MySQL.Product.ProductPriceDAO import ProductPriceDAO
from repositories.data_access.SQL.MySQL.Product.ProductTextDAO import ProductTextDAO
from services.Catalog.ICatalogRepository import ICatalogRepository
from services.Config.IConfigRepository import IConfigRepository
from services.Language.ILanguageRepository import ILanguageRepository
from services.Page.IPageRepository import IPageRepository
from services.Page.IPageTextRepository import IPageTextRepository

services_map: dict[type, type] = {
    # Repository
    ICatalogRepository: CatalogRepository,
    IConfigRepository: ConfigRepository,
    ILanguageRepository: LanguageRepository,
    IPageRepository: PageRepository,
    IPageTextRepository: PageTextRepository,
    # DAO
    IProductDAO: ProductDAO,
    IProductTextDAO: ProductTextDAO,
    IProductPositionDAO: ProductPositionDAO,
    IProductPositionTextDAO: ProductPositionTextDAO,
    IProductPriceDAO: ProductPriceDAO,
    ICurrencyDAO: CurrencyDAO,
}
