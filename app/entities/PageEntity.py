from dataclasses import dataclass
from datetime import datetime


@dataclass
class PageEntity:

    id: int
    code: str
    title: str
    template: str
    is_active: bool
    created_at: datetime
    updated_at: datetime