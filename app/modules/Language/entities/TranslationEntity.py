from dataclasses import dataclass


@dataclass
class TranslationEntity:

    text_ID: int
    translations: dict[str, str]
