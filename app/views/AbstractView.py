from abc import ABC, abstractmethod


class AbstractView(ABC):

    def __init__(self) -> None:
        self._data = {}

    @abstractmethod
    def render(self):
        pass

    def set_data(self, **data):
        self._data.update(data)