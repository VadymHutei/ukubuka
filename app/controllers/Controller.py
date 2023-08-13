from views.ViewFactory import ViewFactory
from service_container import sc


class Controller:

    def __init__(self) -> None:
        self._view_factory: ViewFactory = sc.get(ViewFactory)