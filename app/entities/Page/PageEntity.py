from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from entities.Entity import Entity
from entities.Page.PageTextEntity import PageTextEntity
from exceptions.entities_exception.PageException import PageException


@dataclass
class PageEntity(Entity):

    id: int
    code: str
    title: str
    template: str
    is_active: bool
    created_at: datetime
    updated_at: datetime

    text: Optional[PageTextEntity] = None

    @property
    def title(self) -> str:
        if self.text:
            return self.text.title
        else:
            raise PageException('Page text is not set')