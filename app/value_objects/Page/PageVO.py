from dataclasses import dataclass

from value_objects.ValueObject import ValueObject


@dataclass(kw_only=True)
class PageVO(ValueObject):

    code: str
    template: str
    is_active: bool
    title: str

    layout: str | None = None
