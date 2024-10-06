import inspect

from service_container.ServiceParameters import ServiceParameters


class ServiceContainer:

    def __init__(self):
        self._bindings: dict[type, type] = {}
        self._service_params: dict[type, ServiceParameters] = {}
        self._services: dict = {}

    def _create(self, service_class: type, parameters: dict):
        dependencies = {}
        dependencies.update(parameters)
        service_parameters = inspect.signature(service_class).parameters
        for parameter in service_parameters.values():
            if (
                parameter.name == 'self'
                or parameter.name in dependencies
                or parameter.annotation == inspect.Signature.empty
            ):
                continue

            dependencies[parameter.name] = self.get(parameter.annotation)

        return service_class(**dependencies)

    def bind(self, services_map: dict[type, type]) -> None:
        self._bindings.update(services_map)

    def set_params(self, parameters: dict[type, ServiceParameters]) -> None:
        self._service_params.update(parameters)

    def get(self, service_class: type, **parameters):
        if service_class in self._bindings:
            service_class = self._bindings[service_class]

        is_singleton = (
            True
            if service_class not in self._service_params
            else self._service_params[service_class].is_singleton
        )

        if is_singleton and service_class in self._services:
            return self._services[service_class]

        service = self._create(service_class, parameters)

        if is_singleton:
            self._services[service_class] = service

        return service
