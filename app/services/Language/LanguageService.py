from datetime import datetime

from data_transfer_objects.Language.AddLanguageDTO import AddLanguageDTO
from data_transfer_objects.Language.EditLanguageDTO import EditLanguageDTO
from entities.Language.LanguageEntity import LanguageEntity
from exceptions.entities_exceptions.LanguageException import LanguageException
from services.IService import IService
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageService(IService):

    def __init__(self, language_repository: ILanguageRepository):
        self._language_repository = language_repository

    def find(self, id: int) -> LanguageEntity | None:
        return self._language_repository.find(id)

    def add(self, add_language_dto: AddLanguageDTO) -> bool:
        language = LanguageEntity(
            code=add_language_dto.code,
            name=add_language_dto.name,
            is_active=add_language_dto.is_active,
            created_at=datetime.now(),
        )

        return self._language_repository.add(language)

    def get_by_id(self, id: int) -> LanguageEntity:
        language = self._language_repository.find(id)

        if language is None:
            raise LanguageException('Not found')

        return language

    def get_by_code(self, code: str) -> LanguageEntity:
        language = self._language_repository.find_by_code(code)

        if language is None:
            raise LanguageException('Not found')

        return language

    def find_all(self) -> list[LanguageEntity] | None:
        return self._language_repository.find_all()

    def find_by_code(self, code: str) -> LanguageEntity | None:
        return self._language_repository.find_by_code(code)
    
    def edit_language(self, language_id: int, update_lanugage_DTO: EditLanguageDTO) -> bool:
        language: LanguageEntity = self.find(language_id)

        language.update_from_dict(update_lanugage_DTO.to_dict())

        language.updated_at = datetime.now()

        return self._language_repository.update(language)

    def delete(self, language_id: int):
        return self._language_repository.delete(language_id)

    def delete_by_code(self, code: str):
        return self._language_repository.delete_by_code(code)

    def find_active(self) -> list[LanguageEntity]:
        return self._language_repository.find_active()