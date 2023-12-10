from dataclasses import dataclass

from data_transfer_objects.DataTransferObject import DataTransferObject


@dataclass
class UpdatePageDTO(DataTransferObject):

    id: int
    code: str
    template: str
    layout: str
    is_active: bool