from abc import abstractmethod
from typing import Any

from transformers.Transformer import Transformer


class ResponseTransformer(Transformer):

    @classmethod
    @abstractmethod
    def transform(cls, data: Any | None) -> Any | None:
        pass

    @classmethod
    def transform_collection(cls, data: list[Any] | None) -> list[Any] | None:
        if data is None:
            return None

        return [cls.transform(element) for element in data]