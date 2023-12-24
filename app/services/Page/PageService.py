from datetime import datetime

from data_transfer_objects.Page.AddPageDTO import AddPageDTO
from data_transfer_objects.Page.UpdatePageDTO import UpdatePageDTO
from data_transfer_objects.Page.UpdatePageTranslationDTO import UpdatePageTranslationDTO
from entities.Page.PageEntity import PageEntity
from entities.Page.PageTranslationEntity import PageTranslationEntity
from services.IService import IService
from services.Page.IPageRepository import IPageRepository


class PageService(IService):

    def __init__(self, repository: IPageRepository) -> None:
        self._repository = repository

    def find_all(self) -> list[PageEntity]:
        return self._repository.find_all()

    def add_page(self, add_page_dto: AddPageDTO) -> bool:
        page = PageEntity(
            code=add_page_dto.code,
            template=add_page_dto.template,
            layout=add_page_dto.layout,
            is_active=add_page_dto.is_active,
            created_at=datetime.now()
        )

        return self._repository.add(page)

    def find_by_code(self, code: str) -> PageEntity | None:
        return self._repository.find_by_code(code)

    def update_page(self, update_page_dto: UpdatePageDTO) -> bool:
        page = self._repository.find_by_id(update_page_dto.id)

        page.update_from_dict(update_page_dto.to_dict())

        page.updated_at = datetime.now()

        return self._repository.update(page)

    def update_page_translation(self, update_page_translation_dto: UpdatePageTranslationDTO) -> bool:
        translation = self._repository.find_translation_by_id(update_page_translation_dto.id)

        translation.update_from_dict(update_page_translation_dto.to_dict())

        translation.updated_at = datetime.now()

        return self._repository.update_translation(translation)

    def delete_by_code(self, code: str) -> bool:
        return self._repository.delete_by_code(code)

    def find_translation_by_id(self, id: int) -> PageTranslationEntity | None:
        return self._repository.find_translation_by_id(id)

    def find_translations_by_code(self, code: str) -> list[PageTranslationEntity]:
        return self._repository.find_translations_by_code(code)