from dataclasses import dataclass
from typing import Optional


@dataclass
class UserNameEntity:

    first_name: Optional[str] = None
    last_name: Optional[str] = None
