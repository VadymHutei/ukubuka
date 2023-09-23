from services.Language.LanguageRepositoryInterface import LanguageRepositoryInterface
from services.Service import IService


class LanguageService(IService):

    def __init__(self, repository: LanguageRepositoryInterface) -> None:
        self._repository = repository