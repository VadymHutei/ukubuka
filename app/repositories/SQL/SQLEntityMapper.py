from typing import Type

from entities.Entity import Entity
from exceptions.MapperException import MapperException
from repositories.EntityMapper import EntityMapper
from repositories.MapperCast import MapperCast


class SQLEntityMapper(EntityMapper):

    _ENTITY_CLASS: Type[Entity]
    _TABLE: str
    _TABLE_PREFIX: str
    _FIELDS: list[str]
    _CAST: dict[str, MapperCast] = {}
    _ENTITIES: dict[str, Type[EntityMapper]] = {}

    @classmethod
    @property
    def table(cls) -> str:
        return f'{cls._TABLE} AS {cls._TABLE_PREFIX}'

    @classmethod
    @property
    def table_prefix(cls) -> str:
        return cls._TABLE_PREFIX

    @classmethod
    @property
    def fields(cls) -> str:
        return ',\n'.join([f'{cls._TABLE_PREFIX}.{field} as {cls._TABLE_PREFIX}_{field}' for field in cls._FIELDS])

    @classmethod
    def create_entity(cls, db_record: dict) -> Entity:
        data = {}

        for field in cls._FIELDS:
            field_alias = f'{cls._TABLE_PREFIX}_{field}'

            if field_alias not in db_record:
                raise MapperException(f'Field {field_alias} not found in DB record')

            if field in cls._CAST:
                cast_type: MapperCast = cls._CAST[field]
                value = db_record[field_alias]
                data[field] = MapperCast.cast(cast_type, value)
            else:
                data[field] = db_record[field_alias]

        try:
            for field, mapper in cls._ENTITIES.items():
                entity = mapper.create_entity(db_record)
                data[field] = entity
        except MapperException:
            pass

        return cls._ENTITY_CLASS(**data)

    @classmethod
    def create_entity_tuple(cls, db_records: list[dict]) -> list[Entity]:
        return [cls.create_entity(db_record) for db_record in db_records]