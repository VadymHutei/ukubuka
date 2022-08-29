class LanguageEntity:

    def __init__(self, code: str, name: str, is_active: bool, is_default: bool):
        self.code = code
        self.name = name
        self.is_active = is_active
        self.is_default = is_default
