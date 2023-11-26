from dataclasses import dataclass
from datetime import datetime

from value_objects.IValueObject import IValueObject


@dataclass(kw_only=True)
class LanguageVO(IValueObject):

    code: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None