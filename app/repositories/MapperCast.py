from enum import Enum


def _int(value: str):
    return int(value)

def _bool(value: str):
    return bool(value)


class MapperCast(Enum):

    int = _int
    bool = _bool