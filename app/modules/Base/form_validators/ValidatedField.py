from typing import Optional


class ValidatedField:

    def __init__(self, name, required=True, empty_allowed=False):
        self.name = name
        self.value = None
        self.required = required
        self.empty_allowed = empty_allowed
        self.errors = []
        self.rules = []

    def validate(self, value: Optional[str]):
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
