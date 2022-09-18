import re

from modules.Base.validators.Validator import Validator


class UserValidator(Validator):

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

    @staticmethod
    def email(email):
        if isinstance(email, str):
            return bool(re.fullmatch(r'[^@]+@[^@]+', email))
        return False
