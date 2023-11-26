from entities.Language.LanguageEntity import LanguageEntity
from services.IService import IService
from services.Language.ILanguageRepository import ILanguageRepository
from value_objects.Language.LanguageVO import LanguageVO


class LanguageService(IService):

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository: ILanguageRepository = repository

    def add_language(self, language_vo: LanguageVO) -> bool:
        return self._repository.add(language_vo)

    def find_all(self) -> list[LanguageEntity] | None:
        return self._repository.find_all()

    def find_by_code(self, code: str) -> LanguageEntity | None:
        return self._repository.find_by_code(code)