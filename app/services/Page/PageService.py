from services.IService import IService
from services.Page.PageRepositoryInterface import PageRepositoryInterface
from entities.Page.PageEntity import PageEntity
from exceptions.entities_exceptions.PageException import PageException


class PageService(IService):

    def __init__(self, repository: PageRepositoryInterface) -> None:
        self._repository = repository

    def get_by_code(self, code: str) -> PageEntity:
        page = self._repository.find_by_code(code)

        if not page:
            raise PageException('Page not found')

        return page