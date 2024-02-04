from datetime import datetime

from data_transfer_objects.Page.AddPageDTO import AddPageDTO
from data_transfer_objects.Page.AddPageTranslationDTO import AddPageTranslationDTO
from data_transfer_objects.Page.EditPageDTO import EditPageDTO
from data_transfer_objects.Page.UpdatePageTranslationDTO import UpdatePageTranslationDTO
from entities.Page.PageEntity import PageEntity
from entities.Page.PageTranslationEntity import PageTranslationEntity
from services.IService import IService
from services.Page.IPageRepository import IPageRepository


class PageService(IService):

    def __init__(self, page_repository: IPageRepository) -> None:
        self._page_repository = page_repository

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
        page = self._page_repository.find(page_id)

        page.update_from_dict(edit_page_dto.to_dict())

        page.updated_at = datetime.now()

        return self._page_repository.update(page)

    def update_page_translation(self, update_page_translation_dto: UpdatePageTranslationDTO) -> bool:
        translation = self._page_repository.find_translation(update_page_translation_dto.id)

        translation.update_from_dict(update_page_translation_dto.to_dict())

        translation.updated_at = datetime.now()

        return self._page_repository.update_translation(translation)

    def delete(self, page_id: int):
        return self._page_repository.delete(page_id)

    def delete_by_code(self, code: str) -> bool:
        return self._page_repository.delete_by_code(code)

    def find_translation_by_id(self, page_id: int) -> PageTranslationEntity | None:
        return self._page_repository.find_translation_by_id(page_id)

    def find_translations_by_page_id(self, page_id: int) -> list[PageTranslationEntity]:
        return self._page_repository.find_translations_by_entity_id(page_id)

    def find_translations_by_page_code(self, page_code: str) -> list[PageTranslationEntity]:
        return self._page_repository.find_translations_by_entity_code(page_code)
    
    def add_page_translation(self, page_id: int, data: AddPageTranslationDTO):
        translation = PageTranslationEntity(
            page_id=page_id,
            language_id=data.language_id,
            title=data.title,
            created_at=datetime.now(),
        )

        return self._page_repository.add_translation(translation)