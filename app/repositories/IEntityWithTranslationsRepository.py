from abc import abstractmethod, ABC

from entities.TextEntity import TextEntity


class IEntityWithTranslationsRepository(ABC):

    @abstractmethod
    def find_translation(self, id: int) -> TextEntity | None:
        pass

    @abstractmethod
    def find_translations_by_entity_id(self, entity_id: int) -> list[TextEntity]:
        pass

    @abstractmethod
    def add_translation(self, entity: TextEntity) -> bool:
        pass

    @abstractmethod
    def update_translation(self, text: TextEntity) -> bool:
        pass