from dataclasses import dataclass

from data_transfer_objects.DataTransferObject import DataTransferObject


@dataclass
class UpdatePageTranslationDTO(DataTransferObject):

    id: int
    title: str