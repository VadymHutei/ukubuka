from datetime import datetime

from data_transfer_objects.Page.AddPageDTO import AddPageDTO
from data_transfer_objects.Page.UpdatePageDTO import UpdatePageDTO
from entities.Page.PageEntity import PageEntity
from exceptions.entities_exceptions.PageException import PageException
from services.IService import IService
from services.Page.IPageRepository import IPageRepository


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

    def add_page(self, add_page_dto: AddPageDTO) -> bool:
        page = PageEntity(
            code=add_page_dto.code,
            template=add_page_dto.template,
            layout=add_page_dto.layout,
            is_active=add_page_dto.is_active,
            created_at=datetime.now()
        )

        return self._repository.add(page)

    def find_page_by_code(self, code: str) -> PageEntity | None:
        return self._repository.find_by_code(code)

    def update_page(self, update_page_dto: UpdatePageDTO) -> bool:
        page = self._repository.find_by_id(update_page_dto.id)

        page.update_from_dict(update_page_dto.to_dict())

        page.updated_at = datetime.now()

        return self._repository.update(page)

    def delete_page_by_code(self, code: str) -> bool:
        return self._repository.delete_by_code(code)