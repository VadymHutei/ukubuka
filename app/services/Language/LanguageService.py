from services.Language.LanguageRepositoryInterface import LanguageRepositoryInterface
from services.Service import Service


class LanguageService(Service):

    def __init__(self, repository: LanguageRepositoryInterface) -> None:
        self._repository = repository