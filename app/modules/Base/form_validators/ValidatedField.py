class ValidatedField:

    def __init__(self, name: str, required: bool = True, empty_allowed: bool = False):
        self.name: str = name
        self.value: str|None = None
        self.required: bool = required
        self.empty_allowed: bool = empty_allowed
        self.errors: list = []
        self.rules: list = []

    def validate(self, value: str|None):
        if value is None and self.required:
            self.errors.append(f'{self.name} is required')
            return

        if not isinstance(value, str):
            self.errors.append('Value must be of type string')
            return

        if not value and not self.empty_allowed:
            self.errors.append(f'{self.name} cannot be empty')
            return

        for rule in self.rules:
            if not rule.callback(value):
                self.errors.append(rule.error_message)

        if not self.errors:
            self.value = value
