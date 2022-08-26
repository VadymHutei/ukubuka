from abc import ABC, abstractmethod


class AbstractFormValidator(ABC):

    def __init__(self, form):
        self._fields = self.setRules()
        self._hasErrors = False
        self._errors = {}

        for field in self._fields:
            field.value = form.get(field.name)
            field.validate()
            if field.hasErrors:
                self._addErrors(field.getErrors())

    @property
    def hasErrors(self):
        return self._hasErrors

    @property
    def errors(self):
        return self._errors

    @abstractmethod
    def setRules(self):
        pass

    def _addErrors(self, errors):
        if not self._hasErrors:
            self._hasErrors = True
        self._errors.update(errors)

    def getFormData(self):
        result = {}

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