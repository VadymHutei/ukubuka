from typing import Type

from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper
from repositories.IRepository import IRepository


class SQLRepository(IRepository):

    mapper: Type[SQLEntityMapper] | None
    text_mapper: Type[SQLEntityMapper] | None