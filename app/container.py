from ukubuka.container import Container as BaseContainer

from modules.HomePage.provider import HomePageProvider
from modules.Catalog.provider import CatalogProvider
from modules.Product.provider import ProductProvider


class Container(BaseContainer):

    def _setProviders(self):
        self._addProvider(HomePageProvider)
        self._addProvider(CatalogProvider)
        self._addProvider(ProductProvider)