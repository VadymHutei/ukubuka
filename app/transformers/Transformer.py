from abc import ABC, abstractmethod
from typing import Any


class Transformer(ABC):

    @classmethod
    @abstractmethod
    def transform(cls, data: Any) -> Any:
        pass

    @classmethod
    def transform_collection(cls, data: Any) -> Any:
        if data is None:
            return None

        return [cls.transform(element) for element in data]