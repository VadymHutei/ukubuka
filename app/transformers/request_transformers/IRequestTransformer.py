from abc import abstractmethod
from typing import Any

from werkzeug import Request

from transformers.Transformer import Transformer


class IRequestTransformer(Transformer):

    @classmethod
    @abstractmethod
    def transform(cls, request: Request) -> Any:
        pass