from dataclasses import dataclass
from datetime import datetime


@dataclass
class LanguageEntity:

    id
    code: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime