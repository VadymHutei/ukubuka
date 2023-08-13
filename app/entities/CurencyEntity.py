from dataclasses import dataclass


@dataclass
class CurencyEntity:

    id: int
    code: str
    name: str
    symbol: str