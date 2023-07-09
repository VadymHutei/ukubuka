from dataclasses import dataclass
from typing import Optional


@dataclass
class UserNameEntity:

    first_name: Optional[str] = None
    last_name: Optional[str] = None

    def __str__(self):
        name_list = []
        if self.first_name:
            name_list.append(self.first_name)
        if self.last_name:
            name_list.append(self.last_name)

        return ' '.join(name_list) if name_list else ''