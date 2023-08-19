from services.Service import Service
from services.Page.PageRepositoryInterface import PageRepositoryInterface
from entities.Page.PageEntity import PageEntity
from exceptions.entities_exception.PageException import PageException


class PageService(Service):

    def __init__(self, repository: PageRepositoryInterface) -> None:
        self._repository = repository

    def get_by_code(self, code: str) -> PageEntity:
        page = self._repository.find_by_code(code)

        if not page:
            raise PageException('Page not found')

        return page