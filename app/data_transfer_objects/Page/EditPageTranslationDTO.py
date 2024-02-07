from dataclasses import dataclass

from data_transfer_objects.DataTransferObject import DataTransferObject


@dataclass
class EditPageTranslationDTO(DataTransferObject):

    language_id: int
    title: str