from providers.LanguageProvider import LanguageProvider


class DI_Container:

    def __init__(self) -> None:
        self._providers: list = []
        self._services: dict = {}

    def add_providers(self, providers: list):
        self._providers.extend(providers)
        self._set_services()

    def _set_services(self):
        for provider_class in self._providers:
            provider = provider_class()
            services = provider.register()
            self._services.update(services)

    def get(self, service_class):
        return self._services[service_class]


di_container = DI_Container()
di_container.add_providers([
    LanguageProvider,
])