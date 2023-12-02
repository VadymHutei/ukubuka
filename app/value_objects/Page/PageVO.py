from dataclasses import dataclass
from datetime import datetime

from value_objects.IValueObject import IValueObject


@dataclass(kw_only=True)
class PageVO(IValueObject):

    code: str
    template: str
    is_active: bool
    created_at: datetime
    layout: str | None = None
    updated_at: datetime | None = None