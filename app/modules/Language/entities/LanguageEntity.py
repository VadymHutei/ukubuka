from dataclasses import dataclass


@dataclass
class LanguageEntity:

    code: str
    name: str
    is_active: bool
    is_default: bool
