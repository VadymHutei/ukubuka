from enum import Enum, auto
from typing import Self


class MapperFieldTypes(Enum):

    INT = auto()
    BOOL = auto()

    @classmethod
    def convert(cls, cast_type: Self, value: str):
        match cast_type:
            case cls.INT:
                return int(value) if value is not None else None
            case cls.BOOL:
                return bool(value) if value is not None else None