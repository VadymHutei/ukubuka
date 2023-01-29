from service_container.ServiceContainer import ServiceContainer
from service_container.binding import services_map


sc = ServiceContainer()
sc.bind(services_map)