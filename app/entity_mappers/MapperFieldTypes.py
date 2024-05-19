from enum import Enum, auto
from typing import Self


class MapperFieldTypes(Enum):

    INT = auto()
    BOOL = auto()

    @classmethod
    def convert(cls, cast_type: Self, value: str):
        match cast_type:
            case cls.INT:
                return None if value is None else int(value)
            case cls.BOOL:
                return None if value is None else bool(value)