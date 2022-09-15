from dataclasses import dataclass, field


@dataclass
class TextEntity:

    ID: int
    text: str
    translations: dict[str, str] = field(default_factory=dict)
