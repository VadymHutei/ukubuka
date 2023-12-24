from typing import Any

from entities.Entity import Entity
from entity_mappers.EntityMapper import EntityMapper
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from exceptions.MapperException import MapperException
from value_objects.IValueObject import IValueObject


class SQLEntityMapper(EntityMapper):

    QUERY_PLACEHOLDER = '%s'

    _TABLE: str
    _TABLE_PREFIX: str
    _DATA_FIELDS: list[str]
    _FILLABLE_FIELDS: list[str]
    _FIELD_TYPES: dict[str, MapperFieldTypes] = {}

    @classmethod
    @property
    def table(cls) -> str:
        return cls._TABLE

    @classmethod
    @property
    def table_prefix(cls) -> str:
        return cls._TABLE_PREFIX

    @classmethod
    @property
    def table_as_prefix(cls) -> str:
        return f'{cls._TABLE} AS {cls._TABLE_PREFIX}'

    @classmethod
    @property
    def pr_id_field(cls) -> str:
        return cls.pr_field('id')

    @classmethod
    @property
    def fields(cls) -> str:
        fields = [f'{cls._TABLE_PREFIX}.{field} as {cls.field_alias(field)}' for field in cls._DATA_FIELDS]

        return ',\n'.join(fields)

    @classmethod
    @property
    def fillable_fields(cls) -> str:
        return ', '.join(cls._FILLABLE_FIELDS)

    @classmethod
    def fillable_placeholders(cls) -> str:
        return ', '.join([cls.QUERY_PLACEHOLDER] * len(cls._FILLABLE_FIELDS))

    @classmethod
    def fillable_data(cls, entity: Entity) -> list[str]:
        return [getattr(entity, field) for field in cls._FILLABLE_FIELDS]

    @classmethod
    def pr_field(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}.{field}'

    @classmethod
    def field_alias(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}_{field}'

    @classmethod
    def get_field_value_from_db_record(cls, db_record: dict, field: str):
        field_alias = cls.field_alias(field)

        if field_alias not in db_record:
            raise MapperException(f'Field {field_alias} not found in DB record')

        if field in cls._FIELD_TYPES:
            return MapperFieldTypes.convert(cls._FIELD_TYPES[field], db_record[field_alias])
        else:
            return db_record[field_alias]

    @classmethod
    def create_entity(cls, db_record: dict) -> Entity:
        data = {}

        for field in cls._DATA_FIELDS:
            data[field] = cls.get_field_value_from_db_record(db_record, field)

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
            set_fields_statement.append(f'{field} = {cls.QUERY_PLACEHOLDER}')
            set_field_values.append(getattr(entity, field))

        return ', '.join(set_fields_statement), set_field_values