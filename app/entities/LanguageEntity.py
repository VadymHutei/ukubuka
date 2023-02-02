from dataclasses import dataclass
from typing import Optional


@dataclass
class LanguageEntity:

    code: str
    name: str
    is_active: Optional[bool] = None
    is_default: Optional[bool] = None