from modules.Language.LanguageService import LanguageService
from modules.Language.LanguageRepository import LanguageRepository


class LanguageProvider:

    @staticmethod
    def getResources():
        return {
            LanguageService: (LanguageRepository,),
            LanguageRepository: ()
        }