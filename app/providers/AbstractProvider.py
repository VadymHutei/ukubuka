from abc import ABC, abstractmethod


class AbstractProvider(ABC):

    @abstractmethod
    def register(self):
        pass
