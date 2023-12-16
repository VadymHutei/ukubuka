from datetime import datetime

from data_transfer_objects.Language.AddLanguageDTO import AddLanguageDTO
from data_transfer_objects.Language.UpdateLanguageDTO import UpdateLanguageDTO
from entities.Language.LanguageEntity import LanguageEntity
from services.IService import IService
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageService(IService):

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository: ILanguageRepository = repository

    def add(self, add_language_dto: AddLanguageDTO) -> bool:
        language = LanguageEntity(
            code=add_language_dto.code,
            name=add_language_dto.name,
            is_active=add_language_dto.is_active,
            created_at=datetime.now(),
        )

        return self._repository.add(language)

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