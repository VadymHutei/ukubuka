from typing import Any

from entities.Entity import Entity
from entity_mappers.EntityMapper import EntityMapper
from entity_mappers.MapperFieldTypes import MapperFieldTypes
from exceptions.MapperException import MapperException


class SQLEntityMapper(EntityMapper):

    PLCHLD = '%s'

    def __init__(
        self,
        table: str,
        table_prefix: str,
        fields: list[str],
        fillable_fields: list[str],
        field_types: dict[str, MapperFieldTypes],
    ):
        self._table = table
        self._table_prefix = table_prefix
        self._fields = fields
        self._fillable_fields = fillable_fields
        self._field_types = field_types

    @property
    def table(self) -> str:
        return self._table

    @property
    def table_prefix(self) -> str:
        return self._table_prefix

    @property
    def table_as_prefix(self) -> str:
        return f'{self._table} AS {self._table_prefix}'

    @property
    def pr_id_field(self) -> str:
        return self.pr_field('id')

    @property
    def fields(self) -> str:
        fields = [f'{self._table_prefix}.{field} as {self.field_alias(field)}' for field in self._fields]

        return ',\n'.join(fields)

    @property
    def fillable_fields(self) -> str:
        return ', '.join(self._fillable_fields)

    @property
    def fillable_placeholders(self) -> str:
        return ', '.join([self.PLCHLD] * len(self._fillable_fields))

    def fillable_data(self, entity: Entity) -> list[str]:
        return [getattr(entity, field) for field in self._fillable_fields]

    def pr_field(self, field: str) -> str:
        return f'{self._table_prefix}.{field}'

    def field_alias(self, field: str) -> str:
        return f'{self._table_prefix}_{field}'

    def get_field_value_from_db_record(self, db_record: dict, field: str):
        field_alias = self.field_alias(field)

        if field_alias not in db_record:
            raise MapperException(f'Field {field_alias} not found in DB record')

        if field in self._field_types:
            return MapperFieldTypes.convert(self._field_types[field], db_record[field_alias])
        else:
            return db_record[field_alias]

    def get_set_data(self, entity: Entity) -> tuple[str, list[Any]]:
        set_fields_statement = []
        set_field_values = []
        for field in self._fillable_fields:
            set_fields_statement.append(f'{field} = {self.PLCHLD}')
            set_field_values.append(getattr(entity, field))

        return ', '.join(set_fields_statement), set_field_values