from repositories.SQL.MySQL.MySQLRepository import MySQLRepository
from services.Language.ILanguageRepository import ILanguageRepository


class LanguageRepository(MySQLRepository, ILanguageRepository):
    pass