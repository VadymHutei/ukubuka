from repositories.Language.ILanguageRepository import ILanguageRepository
from repositories.Language.MySQL.LanguageRepository import LanguageRepository


services_map: dict[type, type] = {
    ILanguageRepository: LanguageRepository,
}