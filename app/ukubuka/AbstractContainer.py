from abc import ABC, abstractmethod
from inspect import isclass


class AbstractContainer(ABC):

    _providers = []
    _resources = {}

    def __init__(self):
        self._setProviders()
        self._setResources()

    def get(self, resourceName):
        dependencies = [self.get(dependency.__name__) if isclass(dependency) else dependency for dependency in self._resources[resourceName]['dependencies']]
        return self._resources[resourceName]['class'](*dependencies)

    @abstractmethod
    def _setProviders(self):
        pass

    def _addProviders(self, providers):
        self._providers.extend(providers)

    def _setResources(self):
        for provider in self._providers:
            self._resources.update({resource.__name__: {'class': resource, 'dependencies': dependencies} for resource, dependencies in provider.getResources().items()})