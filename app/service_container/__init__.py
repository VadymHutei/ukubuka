from service_container.ServiceContainer import ServiceContainer
from service_container.binding import services_map
from service_container.parameters import parameters


sc = ServiceContainer()
sc.bind(services_map)
sc.set_params(parameters)
