from entity_mappers.SQL.SQLEntityMapper import SQLEntityMapper


class SQLTextEntityMapper(SQLEntityMapper):

    ENTITY_FOREIGN_KEY_FIELD: str
    LANGUAGE_FOREIGN_KEY_FIELD: str = 'language_id'

    @classmethod
    @property
    def entity_foreign_key_field_with_prefix(cls) -> str:
        return f'{cls._TABLE_PREFIX}.{cls.ENTITY_FOREIGN_KEY_FIELD}'

    @classmethod
    @property
    def language_foreign_key_field_with_prefix(cls) -> str:
        return f'{cls._TABLE_PREFIX}.{cls.LANGUAGE_FOREIGN_KEY_FIELD}'