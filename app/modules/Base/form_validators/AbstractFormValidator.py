from abc import ABC, abstractmethod


class AbstractFormValidator(ABC):

    def __init__(self, form):
        self._fields = self.setRules()
        self.errors = {}

        for field in self._fields:
            field.value = form.get(field.name)
            field.validate()
            if field.hasErrors:
                self.errors.update(field.getErrors())

    @abstractmethod
    def setRules(self):
        pass

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
