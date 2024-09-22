from abc import ABC, abstractmethod
from collections.abc import Iterable
from typing import Any


class Transformer(ABC):

    @classmethod
    @abstractmethod
    def transform(cls, data: Any) -> Any:
        pass

    @classmethod
    def transform_collection(cls, data: Iterable[Any]) -> Any:
        return [cls.transform(element) for element in data]
