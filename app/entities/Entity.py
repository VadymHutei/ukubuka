from dataclasses import dataclass
from typing import Any


@dataclass(kw_only=True)
class Entity:

    id: int | None = None

    def update_from_dict(self, data: dict[str, Any]):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)