from repositories.SQL.SQLRepository import SQLRepository
from services.Language.LanguageRepositoryInterface import LanguageRepositoryInterface


class LanguageRepository(SQLRepository, LanguageRepositoryInterface):
    pass