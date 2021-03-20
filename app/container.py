from ukubuka.AbstractContainer import AbstractContainer

from modules.Language.provider import LanguageProvider
from modules.ACP.provider import ACPProvider
from modules.HomePage.provider import HomePageProvider
from modules.Catalog.provider import CatalogProvider
from modules.Product.provider import ProductProvider
from modules.Shop.provider import ShopProvider


class Container(AbstractContainer):

    def _setProviders(self):
        self._addProviders([
            LanguageProvider,
            ACPProvider,
            HomePageProvider,
            CatalogProvider,
            ProductProvider,
            ShopProvider,
        ])