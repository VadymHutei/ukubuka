import re

from modules.Ukubuka.UkubukaValidator import UkubukaValidator


class UserValidator(UkubukaValidator):

    @staticmethod
    def password(password: str) -> bool:
        if isinstance(password, str):
            return bool(re.fullmatch(r'[\w\W]{3,64}', password))
        return False

    @staticmethod
    def name(name: str) -> bool:
        if isinstance(name, str):
            return bool(re.fullmatch(r'[a-zA-Zа-яА-ЯєЄіІїЇґҐ\']{1,64}', name))
        return False
