from repositories.Language.ILanguageRepository import ILanguageRepository
from repositories.Language.LanguageRepository import LanguageRepository


services_map: dict[type, type] = {
    ILanguageRepository: LanguageRepository,
}