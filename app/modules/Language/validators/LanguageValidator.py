import re

from modules.Ukubuka.UkubukaValidator import UkubukaValidator


class LanguageValidator(UkubukaValidator):

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