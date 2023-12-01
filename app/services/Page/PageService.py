from services.IService import IService
from services.Page.IPageRepository import IPageRepository
from entities.Page.PageEntity import PageEntity
from exceptions.entities_exceptions.PageException import PageException


class PageService(IService):

    def __init__(self, repository: IPageRepository) -> None:
        self._repository = repository

    def get_by_code(self, code: str) -> PageEntity:
        page = self._repository.find_by_code(code)

        if not page:
            raise PageException('Page not found')

        return page

    def get_all(self) -> list[PageEntity]:
        return self._repository.get_all()