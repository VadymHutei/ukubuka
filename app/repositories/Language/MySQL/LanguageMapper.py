from entities.Language import Language
from repositories.IMapper import IMapper


class LanguageMapper(IMapper):

    def from_row(self, row: dict) -> Language:
        return Language(
            code=row['code'],
            name=row['name'],
            is_active=row['is_active'],
            is_default=row['is_default'],
        )

    def from_rows(self, rows: list|tuple) -> dict[str, Language]:
        languages = {}

        for row in rows:
            language = self.from_row(row)
            languages[language.code] = language

        return languages