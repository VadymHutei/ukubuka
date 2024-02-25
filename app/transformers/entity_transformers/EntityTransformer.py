from abc import abstractmethod
from typing import Any

from entities.Entity import Entity
from transformers.Transformer import Transformer


class EntityTransformer(Transformer):

    @abstractmethod
    def transform(self, data: Any) -> Entity:
        pass
