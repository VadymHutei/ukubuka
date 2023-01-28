from dataclasses import dataclass
from typing import Optional


@dataclass
class Language:

    code: str
    name: str
    is_active: Optional[bool] = None
    is_default: Optional[bool] = None