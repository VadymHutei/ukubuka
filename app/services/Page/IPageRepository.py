from abc import ABC, abstractmethod

from entities.Page.PageEntity import PageEntity


class IPageRepository(ABC):

    @abstractmethod
    def find_by_code(self, code: str) -> PageEntity:
        pass

    @abstractmethod
    def get_all(self) -> list[PageEntity]:
        pass