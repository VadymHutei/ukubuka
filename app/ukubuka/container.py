from abc import ABC, abstractmethod


class BaseContainer(ABC):

    _providers = []

    def __init__(self):
        self._setProviders()
        self._setResources()

    def get(self, resourceName):
        dependencies = [self.get(dependency.__name__) for dependency in self.__dict__[resourceName]['dependencies']]
        return self.__dict__[resourceName]['class'](*dependencies)

    @abstractmethod
    def _setProviders(self):
        pass

    def _addProvider(self, provider):
        self._providers.append(provider)

    def _setResources(self):
        for provider in self._providers:
            self.__dict__.update({resource.__name__: {'class': resource, 'dependencies': dependencies} for resource, dependencies in provider.getResources().items()})