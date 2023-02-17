from entities.LanguageEntity import LanguageEntity
from repositories.Language.ILanguageRepository import ILanguageRepository


class LanguageService:

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository = repository

    def get_languages(self) -> dict[str, LanguageEntity]:
        return self._repository.find_all()