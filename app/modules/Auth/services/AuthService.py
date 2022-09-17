from random import choice as random_choice


class AuthService:

    @staticmethod
    def get_random_string(length: int, abc: str) -> str:
        return ''.join([random_choice(abc) for _ in range(length)])
