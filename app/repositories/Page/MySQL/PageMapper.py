from entities.PageEntity import PageEntity
from repositories.IMapper import IMapper


class PageMapper(IMapper):

    def from_row(self, row: dict) -> PageEntity:
        return PageEntity(
            id=int(row['id']),
            code=row['code'],
            title=row['title'],
            template=row['template'],
            is_active=bool(row['is_active']),
            created_at=row['created_at'],
            updated_at=row['updated_at'],
        )

    def from_rows(self, rows: list|tuple) -> dict[str, PageEntity]:
        pages = {}

        for row in rows:
            page = self.from_row(row)
            pages[page.code] = page

        return pages