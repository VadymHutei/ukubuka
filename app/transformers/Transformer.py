from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any


class Transformer(ABC):

    @abstractmethod
    def transform(self, data: Any) -> Any:
        pass

    def transform_collection(self, data: Iterable[Any]) -> Any:
        return [self.transform(element) for element in data]
