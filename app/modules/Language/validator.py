import re


class LanguageValidator:

    @staticmethod
    def languageCode(code):
        if isinstance(code, str):
            return bool(re.fullmatch(r'[a-zA-Z]{3}', code))
        return False