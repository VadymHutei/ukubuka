from repositories.Mapper import Mapper
from entities.Entity import Entity


class SQLMapper(Mapper):

    _ENTITY_CLASS: type
    _TABLE_PREFIX: str
    _FIELDS: list[str]
    _CAST: dict[str, str]

    @classmethod
    def get_fields(cls) -> str:
        return ',\n'.join([f'{cls._TABLE_PREFIX}.{field} as {cls._TABLE_PREFIX}_{field}' for field in cls._FIELDS])

    @classmethod
    def create_entity(cls, db_record: dict) -> Entity:
        data = {
            field: cls._CAST[field](db_record[cls._get_field_name(field)])
            if field in cls._CAST
            else db_record[cls._get_field_name(field)]
            for field in cls._FIELDS
        }

        entity = cls._ENTITY_CLASS(**data)

        return entity

    @classmethod
    def _get_field_name(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}_{field}'