from datetime import datetime

from data_transfer_objects.Page.UpdatePageDTO import UpdatePageDTO
from entities.Page.PageEntity import PageEntity
from exceptions.entities_exceptions.PageException import PageException
from services.IService import IService
from services.Page.IPageRepository import IPageRepository
from value_objects.Page.PageVO import PageVO


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

    def add_page(self, vo: PageVO) -> bool:
        return self._repository.add(vo)

    def find_by_code(self, code: str) -> PageEntity | None:
        return self._repository.find_by_code(code)

    def update(self, update_page_dto: UpdatePageDTO) -> bool:
        page = self._repository.find_by_id(update_page_dto.id)

        page.update_from_dict(update_page_dto.to_dict())

        page.updated_at = datetime.now()

        return self._repository.update(page)