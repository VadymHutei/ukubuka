from abc import abstractmethod, ABC

from entities.Entity import Entity


class ICodeRepository(ABC):

    @abstractmethod
    def find_by_code(self, code: str) -> Entity | None:
        pass

    @abstractmethod
    def delete_by_code(self, code: str) -> bool:
        pass