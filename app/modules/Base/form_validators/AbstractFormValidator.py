from abc import ABC, abstractmethod

from modules.Base.form_validators.ValidatedField import ValidatedField


class AbstractFormValidator(ABC):

    def __init__(self, form):
        self._fields: tuple[ValidatedField] = self._set_field_validation_rules()
        self.errors: dict[str, list] = {}

        self._validate(form)

    @abstractmethod
    def _set_field_validation_rules(self):
        pass

    def _validate(self, form):
        for field in self._fields:
            field.validate(form[field.name])
            if field.errors:
                self.errors.update({field.name: field.errors})

    def get_form_data(self) -> dict[str, str]:
        return {field.name: field.value for field in self._fields if not field.errors}
