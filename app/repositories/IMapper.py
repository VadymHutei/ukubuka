from abc import ABC, abstractmethod


class IMapper(ABC):
    
    @abstractmethod
    def from_row(self, row: dict):
        pass

    @abstractmethod
    def from_rows(self, rows: list):
        pass