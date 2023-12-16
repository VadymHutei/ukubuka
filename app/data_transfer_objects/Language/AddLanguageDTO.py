from dataclasses import dataclass

from data_transfer_objects.DataTransferObject import DataTransferObject


@dataclass
class AddLanguageDTO(DataTransferObject):

    code: str
    name: str
    is_active: bool