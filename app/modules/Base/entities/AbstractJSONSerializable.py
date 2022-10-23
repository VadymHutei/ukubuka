from abc import ABC, abstractmethod
import json


class AbstractJSONSerializable(ABC):

    @abstractmethod
    def to_JSON(self) -> str:
        pass

    @classmethod
    def from_JSON(cls, json_data: str):
        return cls(**json.loads(json_data))