from abc import ABC, abstractmethod

from repositories.IRepository import IRepository


class IPageTextRepository(IRepository, ABC):

    @abstractmethod
    def find_by_page_id(self, page_id: int):
        pass
