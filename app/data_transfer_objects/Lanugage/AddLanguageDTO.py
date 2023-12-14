from dataclasses import dataclass
from datetime import datetime

from data_transfer_objects.DataTransferObject import DataTransferObject


@dataclass
class AddLanguageDTO(DataTransferObject):

    code: str
    name: str
    is_active: bool
    created_at: datetime
    updated_at: datetime | None = None