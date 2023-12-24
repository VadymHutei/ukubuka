from abc import ABC
from typing import Type

from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from entity_mappers.SQL.SQLTextEntityMapper import SQLTextEntityMapper


class SQLRepository(ABC):

    mapper: Type[SQLEntityMapper] | None
    text_mapper: Type[SQLTextEntityMapper] | None