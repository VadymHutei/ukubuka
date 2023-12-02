from datetime import datetime

from data_transfer_objects.Lanugage.UpdateLanguageDTO import UpdateLanguageDTO
from entities.Language.LanguageEntity import LanguageEntity
from services.IService import IService
from services.Language.ILanguageRepository import ILanguageRepository
from value_objects.Language.LanguageVO import LanguageVO


class LanguageService(IService):

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository: ILanguageRepository = repository

    def add(self, language_vo: LanguageVO) -> bool:
        return self._repository.add(language_vo)

    def get_by_id(self, id: int) -> LanguageEntity:
        return self._repository.get_by_id(id)

    def get_by_code(self, code: str) -> LanguageEntity:
        return self._repository.get_by_code(code)

    def find_all(self) -> list[LanguageEntity] | None:
        return self._repository.find_all()
    
    def find_by_id(self, id: int) -> LanguageEntity | None:
        return self._repository.find_by_id(id)

    def find_by_code(self, code: str) -> LanguageEntity | None:
        return self._repository.find_by_code(code)
    
    def update(self, update_lanugage_DTO: UpdateLanguageDTO) -> bool:
        language = self.find_by_id(update_lanugage_DTO.id)

        language.update_from_dict(update_lanugage_DTO.to_dict())

        language.updated_at = datetime.now()

        return self._repository.update(language)

    def delete_by_code(self, code: str):
        return self._repository.delete_by_code(code)

    def get_available(self) -> list[LanguageEntity]:
        return self._repository.get_only_active()