from abc import ABC, abstractmethod

from entities.Config.ConfigEntity import ConfigEntity


class IConfigRepository(ABC):

    @abstractmethod
    def get_config(self) -> list[ConfigEntity]:
        pass