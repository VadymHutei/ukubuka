from abc import ABC
from typing import Type

from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.IRepository import IRepository


class SQLRepository(IRepository, ABC):

    mapper: Type[SQLEntityMapper] | None
    text_mapper: Type[SQLEntityMapper] | None