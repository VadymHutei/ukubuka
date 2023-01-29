from entities.Page import Page
from repositories.Page.MySQL.PageRepository import PageRepository

class PageService:

    def __init__(self, repository: PageRepository) -> None:
        self._repository = repository

    def get_by_code(self, code: str) -> Page:
        return self._repository.find_by_code(code)