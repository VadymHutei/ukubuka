from modules.Base.form_validators.ValidationRule import ValidationRule


class ValidatedField:

    def __init__(self, name, required=True, emptyAllowed=False):
        self.name = name
        self.value = None
        self.required = required
        self.emptyAllowed = emptyAllowed
        self.errors = []
        self._rules = []

    def addRule(self, rule: ValidationRule):
        self._rules.append(rule)

    def validate(self):
        if self.value is None:
            if self.required:
                self.errors.append(f'{self.name} is required')

        if isinstance(self.value, str) and not self.value:
            if not self.emptyAllowed and self.required:
                self.errors.append(f'{self.name} cannot be empty')

        else:
            for rule in self._rules:
                if not rule.callback(self.value):
                    self.errors.append(rule.error_message)
