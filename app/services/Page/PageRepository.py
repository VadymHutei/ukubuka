from abc import ABC, abstractmethod

from entities.Page.PageEntity import PageEntity


class PageRepository(ABC):

    @abstractmethod
    def find_by_code(self, code: str) -> PageEntity:
        pass