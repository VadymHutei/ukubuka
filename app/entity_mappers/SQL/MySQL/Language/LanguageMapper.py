from entities.Language.LanguageEntity import LanguageEntity
from entity_mappers.EntityMapper import EntityMapper


class LanguageMapper(EntityMapper):

    def from_row(self, row: dict) -> LanguageEntity:
        return LanguageEntity(
            code=row['code'],
            name=row['name'],
            is_active=row['is_active'],
        )

    def from_rows(self, rows: list|tuple) -> dict[str, LanguageEntity]:
        languages = {}

        for row in rows:
            language = self.from_row(row)
            languages[language.code] = language

        return languages