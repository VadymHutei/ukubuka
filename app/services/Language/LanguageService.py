from services.IService import IService
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageService(IService):

    def __init__(self, repository: ILanguageRepository) -> None:
        self._repository: ILanguageRepository = repository