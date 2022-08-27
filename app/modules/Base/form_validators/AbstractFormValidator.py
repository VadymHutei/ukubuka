from abc import ABC, abstractmethod


class AbstractFormValidator(ABC):

    def __init__(self):
        self._fields = self._set_field_validation_rules()
        self.errors = {}

    @abstractmethod
    def _set_field_validation_rules(self):
        pass

    def validate(self, form):
        for field in self._fields:
            field.value = form.get(field.name)
            field.validate()
            if field.errors:
                self.errors.update({field.name: field.errors})

    def getFormData(self):
        for field in self._fields:
            if field.required and field.emptyAllowed:
                pass
            if field.required and not field.emptyAllowed:
                pass
            if not field.required and field.emptyAllowed:
                pass
            if not field.required and not field.emptyAllowed:
                pass

        return {field.name: field.value for field in self._fields}
