from datetime import datetime

from data_transfer_objects.Page.AddPageDTO import AddPageDTO
from data_transfer_objects.Page.AddPageTranslationDTO import AddPageTranslationDTO
from data_transfer_objects.Page.EditPageDTO import EditPageDTO
from data_transfer_objects.Page.EditPageTranslationDTO import EditPageTranslationDTO
from entities.Page.PageEntity import PageEntity
from entities.Page.PageTextEntity import PageTextEntity
from repositories.SQL.MySQL.Page.PageTextRepository import PageTextRepository
from services.Service import Service
from services.Page.IPageRepository import IPageRepository


class PageService(Service):

    def __init__(self, page_repository: IPageRepository, page_text_repository: PageTextRepository):
        self._page_repository = page_repository
        self._page_text_repository = page_text_repository

    def find(self, page_id: int) -> PageEntity | None:
        return self._page_repository.find(page_id)

    def find_all(self) -> list[PageEntity]:
        return self._page_repository.find_all()

    def add_page(self, add_page_dto: AddPageDTO) -> bool:
        page = PageEntity(
            code=add_page_dto.code,
            template=add_page_dto.template,
            layout=add_page_dto.layout,
            is_active=add_page_dto.is_active,
            created_at=datetime.now()
        )

        return self._page_repository.add(page)

    def find_by_code(self, code: str) -> PageEntity | None:
        return self._page_repository.find_by_code(code)

    def edit_page(self, page_id: int, edit_page_dto: EditPageDTO) -> bool:
        page: PageEntity = self.find(page_id)

        page.update_from_dict(edit_page_dto.to_dict())

        page.updated_at = datetime.now()

        return self._page_repository.update(page)

    def add_page_translation(self, page_id: int, data: AddPageTranslationDTO) -> bool:
        translation = PageTextEntity(
            page_id=page_id,
            language_id=data.language_id,
            title=data.title,
            created_at=datetime.now(),
        )

        return self._page_repository.add_translation(translation)

    def edit_page_translation(
        self,
        translation_id: int,
        edit_page_translation_dto: EditPageTranslationDTO,
    ) -> bool:
        translation: PageTextEntity = self.find_translation(translation_id)

        translation.update_from_dict(edit_page_translation_dto.to_dict())

        translation.updated_at = datetime.now()

        return self._page_repository.update_translation(translation)

    def delete(self, page_id: int):
        return self._page_repository.delete(page_id)

    def delete_by_code(self, code: str) -> bool:
        return self._page_repository.delete_by_code(code)

    def find_translation(self, translation_id: int) -> PageTextEntity | None:
        return self._page_repository.find_translation(translation_id)

    def find_translations(self, page_id: int) -> list[PageTextEntity]:
        return self._page_text_repository.find_by_page_id(page_id)
