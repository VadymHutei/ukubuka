import re

from modules.Base.validators.Validator import Validator


class LanguageValidator(Validator):

    @staticmethod
    def languageCode(code):
        if isinstance(code, str):
            return bool(re.fullmatch(r'[a-zA-Z]{3}', code))
        return False

    @staticmethod
    def textID(ID):
        return LanguageValidator.intID(ID, True)

    @staticmethod
    def translation(translation):
        if isinstance(translation, str):
            return len(translation) <= 2048
        return False
