from abc import ABC, abstractmethod

from entities.Page.PageEntity import PageEntity


class IPageRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: int) -> PageEntity | None:
        pass

    @abstractmethod
    def find_by_code(self, code: str) -> PageEntity | None:
        pass

    @abstractmethod
    def get_all(self) -> list[PageEntity]:
        pass

    @abstractmethod
    def add(self, page: PageEntity) -> bool:
        pass

    @abstractmethod
    def update(self, page: PageEntity) -> bool:
        pass

    @abstractmethod
    def delete_by_code(self, code: str) -> bool:
        pass