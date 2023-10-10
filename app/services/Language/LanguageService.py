from entities.Language.LanguageEntity import LanguageEntity
from services.IService import IService
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageService(IService):

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository: ILanguageRepository = repository

    def get_all(self, with_inactive: bool = False) -> list[LanguageEntity]:
        return self._repository.get_all(with_inactive)