from abc import abstractmethod, ABC
from typing import TypeVar, Generic

from entities.Entity import Entity

T = TypeVar('T', bound=Entity)


class Builder(Generic[T], ABC):

    @abstractmethod
    def build(self, entity_id: int) -> T:
        pass
