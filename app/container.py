from ukubuka.container import Container as BaseContainer

from modules.hello.provider import HelloProvider
from modules.HomePage.provider import HomePageProvider


class Container(BaseContainer):

    def _setProviders(self):
        self._addProvider(HelloProvider)
        self._addProvider(HomePageProvider)