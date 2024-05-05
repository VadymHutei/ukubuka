from entity_mappers.MapperFieldTypes import MapperFieldTypes
from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper


class SQLTextEntityMapper(SQLEntityMapper):

    LANGUAGE_FOREIGN_KEY_FIELD: str = 'language_id'

    def __init__(
        self,
        table: str,
        table_prefix: str,
        fields: list[str],
        fillable_fields: list[str],
        entity_foreign_key_field: str,
        field_types: dict[str, MapperFieldTypes] = {},
    ):
        super().__init__(
            table,
            table_prefix,
            fields,
            fillable_fields,
            field_types,
        )

        self._entity_foreign_key_field = entity_foreign_key_field

    @property
    def pr_entity_foreign_key_field(self) -> str:
        return f'{self._table_prefix}.{self._entity_foreign_key_field}'

    @property
    def pr_language_foreign_key_field(self) -> str:
        return f'{self._table_prefix}.{self.LANGUAGE_FOREIGN_KEY_FIELD}'
