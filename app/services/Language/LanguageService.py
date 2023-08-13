from typing import Optional
from entities.Language.LanguageEntity import LanguageEntity
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageService:

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository = repository

    def get_languages(self) -> dict[str, LanguageEntity]:
        return self._repository.find_all()
    
    def find_by_code(self, code: str) -> Optional[LanguageEntity]:
        return self._repository.find_by_code(code)