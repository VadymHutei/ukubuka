from abc import ABC, abstractmethod


class AbstractView(ABC):

    @abstractmethod
    def render(self):
        pass