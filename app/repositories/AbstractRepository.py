from abc import ABC, abstractmethod


class AbstractRepository(ABC):

    @abstractmethod
    def find_all(self):
        pass