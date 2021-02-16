from ukubuka.AbstractContainer import AbstractContainer

from modules.HomePage.provider import HomePageProvider
from modules.Catalog.provider import CatalogProvider
from modules.Product.provider import ProductProvider


class Container(AbstractContainer):

    def _setProviders(self):
        self._addProvider(HomePageProvider)
        self._addProvider(CatalogProvider)
        self._addProvider(ProductProvider)