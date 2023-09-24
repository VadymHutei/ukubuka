from services.Language.LanguageRepositoryInterface import LanguageRepositoryInterface
from services.IService import IService


class LanguageService(IService):

    def __init__(self, repository: LanguageRepositoryInterface) -> None:
        self._repository = repository