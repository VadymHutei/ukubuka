from ukubuka.container import Container as BaseContainer

from modules.hello.provider import HelloProvider


class Container(BaseContainer):

    def _setProviders(self):
        self._addProvider(HelloProvider)