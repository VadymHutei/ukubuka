from abc import ABC, abstractmethod


class BaseContainer(ABC):

    _providers = []

    def __init__(self):
        self._setProviders()
        self._setResources()

    def get(self, resourceName):
        dependencies = []
        for dependency in self.__dict__[resourceName]['dependencies']:
            dependencies.append(self.get(dependency.__name__))
        return self.__dict__[resourceName]['class'](*dependencies)

    @abstractmethod
    def _setProviders(self):
        pass

    def _addProvider(self, provider):
        self._providers.append(provider)

    def _setResources(self):
        for provider in self._providers:
            for resource, dependencies in provider.getResources().items():
                setattr(
                    self,
                    resource.__name__,
                    {
                        'class': resource,
                        'dependencies': dependencies
                    }
                )