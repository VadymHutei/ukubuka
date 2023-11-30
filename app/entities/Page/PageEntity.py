from dataclasses import dataclass
from datetime import datetime

from entities.Entity import Entity
from entities.Page.PageTextEntity import PageTextEntity
from exceptions.entities_exceptions.PageException import PageException


@dataclass
class PageEntity(Entity):

    id: int
    code: str
    template: str
    layout: str | None
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None

    text: PageTextEntity | None = None

    @property
    def title(self) -> str:
        if self.text:
            return self.text.title
        else:
            raise PageException('Page text is not set')