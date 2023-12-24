from abc import abstractmethod, ABC

from entities.TextEntity import TextEntity


class ITextRepository(ABC):

    @abstractmethod
    def find_translation(self, id: int) -> TextEntity | None:
        pass

    @abstractmethod
    def update_translation(self, text: TextEntity) -> bool:
        pass