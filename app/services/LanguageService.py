from repositories.LanguageRepository import LanguageRepository


class LanguageService:

    def __init__(self, repository: LanguageRepository) -> None:
        self._repository = repository

    def get_languages(self):
        return self._repository.find_all()