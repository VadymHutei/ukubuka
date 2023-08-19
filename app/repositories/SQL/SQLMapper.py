from typing import Type

from exceptions.MapperException import MapperException
from repositories.Mapper import Mapper
from entities.Entity import Entity
from repositories.MapperCast import MapperCast


class SQLMapper(Mapper):

    _ENTITY_CLASS: Type[Entity]
    _TABLE: str
    _TABLE_PREFIX: str
    _FIELDS: list[str]
    _CAST: dict[str, MapperCast] = {}
    _ENTITIES: dict[str, Type[Mapper]] = {}

    @classmethod
    def get_fields(cls) -> str:
        return ',\n'.join([f'{cls._TABLE_PREFIX}.{field} as {cls._TABLE_PREFIX}_{field}' for field in cls._FIELDS])
    
    @classmethod
    def get_table(cls) -> str:
        return f'{cls._TABLE} AS {cls._TABLE_PREFIX}'

    @classmethod
    def create_entity(cls, db_record: dict) -> Entity:
        data = {}

        for field in cls._FIELDS:
            field_alias = f'{cls._TABLE_PREFIX}_{field}'

            if field_alias not in db_record:
                raise MapperException(f'Field {field_alias} not found in DB record')

            if field in cls._CAST:
                data[field] = cls._CAST[field].value(db_record[field_alias])
            else:
                data[field] = db_record[field_alias]

        try:
            for field, mapper in cls._ENTITIES.items():
                entity = mapper.create_entity(db_record)
                data[field] = entity
        except MapperException:
            pass

        return cls._ENTITY_CLASS(**data)