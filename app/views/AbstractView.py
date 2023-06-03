from abc import ABC, abstractmethod


class AbstractView(ABC):

    def __init__(self) -> None:
        self._data: dict = {}

    @abstractmethod
    def render(self) -> str:
        pass