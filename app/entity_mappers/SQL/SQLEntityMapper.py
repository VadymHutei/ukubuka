from typing import Any

from data_transfer_objects.DataTransferObject import DataTransferObject
from entities.Entity import Entity
from entity_mappers.EntityMapper import EntityMapper
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from exceptions.MapperException import MapperException
from value_objects.IValueObject import IValueObject


class SQLEntityMapper(EntityMapper):

    _TABLE: str
    _TABLE_PREFIX: str
    _DATA_FIELDS: list[str]
    _FILLABLE_FIELDS: list[str]
    _FIELD_TYPES: dict[str, MapperFieldTypes] = {}
    _QUERY_PLACEHOLDER = '%s'

    @classmethod
    @property
    def table(cls) -> str:
        return cls._TABLE

    @classmethod
    @property
    def table_as_prefix(cls) -> str:
        return f'{cls._TABLE} AS {cls._TABLE_PREFIX}'

    @classmethod
    @property
    def table_prefix(cls) -> str:
        return cls._TABLE_PREFIX

    @classmethod
    @property
    def fields(cls) -> str:
        fields = [f'{cls._TABLE_PREFIX}.{field} as {cls._get_field_alias(field)}' for field in cls._DATA_FIELDS]

        return ',\n'.join(fields)

    @classmethod
    @property
    def fillable(cls) -> str:
        return ', '.join(cls._FILLABLE_FIELDS)

    @classmethod
    @property
    def fillable_length(cls) -> int:
        return len(cls._FILLABLE_FIELDS)

    @classmethod
    def fillable_placeholders(cls) -> str:
        return ', '.join([cls._QUERY_PLACEHOLDER] * len(cls._FILLABLE_FIELDS))

    @classmethod
    def fillable_data(cls, obj: DataTransferObject) -> list[str]:
        return [getattr(obj, field) for field in cls._FILLABLE_FIELDS]

    @classmethod
    def field(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}.{field}'

    @classmethod
    def _get_field_alias(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}_{field}'

    @classmethod
    def create_entity(cls, db_record: dict) -> Entity | IValueObject:
        data = {}

        for field in cls._DATA_FIELDS:
            field_alias = cls._get_field_alias(field)

            if field_alias not in db_record:
                raise MapperException(f'Field {field_alias} not found in DB record')

            if field in cls._FIELD_TYPES:
                data[field] = MapperFieldTypes.convert(cls._FIELD_TYPES[field], db_record[field_alias])
            else:
                data[field] = db_record[field_alias]

        try:
            for field, mapper in cls._NESTED_ENTITY_MAPPERS.items():
                entity = mapper.create_entity(db_record)
                data[field] = entity
        except MapperException:
            pass

        return cls._ENTITY_CLASS(**data)

    @classmethod
    def create_entities(cls, db_records: list[dict]) -> list[Entity | IValueObject]:
        return [cls.create_entity(db_record) for db_record in db_records]

    @classmethod
    def get_set_data(cls, entity: Entity) -> tuple[str, list[Any]]:
        set_fields_statement = []
        set_field_values = []
        for field in cls._FILLABLE_FIELDS:
            set_fields_statement.append(f'{field} = {cls._QUERY_PLACEHOLDER}')
            set_field_values.append(getattr(entity, field))

        return ', '.join(set_fields_statement), set_field_values