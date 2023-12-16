from abc import abstractmethod
from typing import Any

from flask import Request

from transformers.Transformer import Transformer


class RequestTransformer(Transformer):

    @classmethod
    @abstractmethod
    def transform(cls, request: Request) -> Any:
        pass