from modules.Base.form_validators.ValidationRule import ValidationRule


class ValidatedField:

    def __init__(self, name, required=True, empty_allowed=False):
        self.name = name
        self.value = None
        self.required = required
        self.empty_allowed = empty_allowed
        self.errors = []
        self._rules = []

    def add_rule(self, rule: ValidationRule):
        self._rules.append(rule)

    def validate(self):
        if self.value is None:
            if self.required:
                self.errors.append(f'{self.name} is required')

        if isinstance(self.value, str) and not self.value:
            if not self.empty_allowed and self.required:
                self.errors.append(f'{self.name} cannot be empty')

        else:
            for rule in self._rules:
                if not rule.callback(self.value):
                    self.errors.append(rule.error_message)
