import inspect


class ServiceContainer:

    _services: dict = {}

    def _create(self, service_class: type, dependencies: dict = {}):
        d = {}
        d.update(dependencies)
        service_parametert = inspect.signature(service_class).parameters
        for parameter in service_parametert.values():
            if parameter.name == 'self':
                continue
            if parameter.annotation == inspect._empty:
                continue
            d[parameter.name] = self.get(parameter.annotation)

        return service_class(**d)

    def get(self, service_class: type, dependencies: dict = {}):
        if service_class in self._services:
            return self._services[service_class]

        service = self._create(service_class, dependencies)
        self._services[service_class] = service

        return self._services[service_class]