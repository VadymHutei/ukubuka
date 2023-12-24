from dataclasses import dataclass
from datetime import datetime

from entities.Catalog.CatalogTextEntity import CatalogTextEntity
from entities.Entity import Entity
from exceptions.entities_exceptions.CatalogException import CatalogException


@dataclass
class CatalogEntity(Entity):

    code: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None
    deleted_at: datetime | None = None

    text: CatalogTextEntity | None = None

    @property
    def name(self) -> str:
        if self.text:
            return self.text.name
        else:
            raise CatalogException('Catalog text data is not set')

    @property
    def description(self)-> str:
        if self.text:
            return self.text.description
        else:
            raise CatalogException('Catalog text data is not set')