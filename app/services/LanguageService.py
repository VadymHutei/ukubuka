from entities.Language import Language
from repositories.Language.ILanguageRepository import ILanguageRepository


class LanguageService:

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository = repository

    def get_languages(self) -> dict[str, Language]:
        return self._repository.find_all()