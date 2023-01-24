from repositories.LanguageRepository import LanguageRepository
from providers.AbstractProvider import AbstractProvider
from services.LanguageService import LanguageService


class LanguageProvider(AbstractProvider):

    def register(self):
        language_repository = LanguageRepository()
        language_service = LanguageService(language_repository)
        return {
            LanguageRepository: language_repository,
            LanguageService: language_service,
        }
