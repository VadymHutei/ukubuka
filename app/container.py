from ukubuka.container import BaseContainer

from modules.hello.provider import HelloProvider


class Container(BaseContainer):

    def _setProviders(self):
        self._addProvider(HelloProvider)