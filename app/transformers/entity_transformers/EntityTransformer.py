from typing import Any

from entities.Entity import Entity
from transformers.Transformer import Transformer


class EntityTransformer(Transformer):

    @classmethod
    def transform(cls, data: Any) -> Entity:
        pass