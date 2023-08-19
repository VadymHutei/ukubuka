from enum import Enum, auto
from typing import Self


class MapperCast(Enum):

    INT = auto()
    BOOL = auto()

    @classmethod
    def cast(cls, cast_type: Self, value: str):
        match cast_type:
            case cls.INT:
                return int(value)
            case cls.BOOL:
                return bool(value)