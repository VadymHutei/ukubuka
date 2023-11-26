from entities.IEntity import IEntity
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
    def fillable_data(cls, obj: IValueObject) -> list[str]:
        return [getattr(obj, field) for field in cls._FILLABLE_FIELDS]

    @classmethod
    def field(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}.{field}'

    @classmethod
    def _get_field_alias(cls, field: str) -> str:
        return f'{cls._TABLE_PREFIX}_{field}'

    @classmethod
    def create_entity(cls, db_record: dict) -> IEntity | IValueObject:
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
    def create_entities(cls, db_records: list[dict]) -> list[IEntity | IValueObject]:
        return [cls.create_entity(db_record) for db_record in db_records]