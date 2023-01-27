import inspect


class ServiceContainer:

    _services: dict = {}

    def _create(self, service_class):
        dependencies = {}
        service_parametert = inspect.signature(service_class).parameters
        for parameter in service_parametert.values():
            if parameter.name == 'self':
                continue
            if parameter.annotation == inspect._empty:
                continue
            dependencies[parameter.name] = self.get(parameter.annotation)

        return service_class(**dependencies)

    def get(self, service_class):
        if service_class in self._services:
            return self._services[service_class]

        service = self._create(service_class)
        self._services[service_class] = service

        return self._services[service_class]