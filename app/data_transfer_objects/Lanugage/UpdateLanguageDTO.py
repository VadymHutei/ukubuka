from dataclasses import dataclass

from data_transfer_objects.DataTransferObject import DataTransferObject


@dataclass
class UpdateLanguageDTO(DataTransferObject):

    id: int
    code: str
    name: str
    is_active: bool