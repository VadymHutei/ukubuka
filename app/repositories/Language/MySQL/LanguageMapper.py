from entities.LanguageEntity import LanguageEntity
from repositories.IMapper import IMapper


class LanguageMapper(IMapper):

    def from_row(self, row: dict) -> LanguageEntity:
        return LanguageEntity(
            code=row['code'],
            name=row['name'],
            is_active=row['is_active'],
            is_default=row['is_default'],
        )

    def from_rows(self, rows: list|tuple) -> dict[str, LanguageEntity]:
        languages = {}

        for row in rows:
            language = self.from_row(row)
            languages[language.code] = language

        return languages