from abc import ABC, abstractclassmethod


class AbstractTransformer(ABC):

    @abstractclassmethod
    def transform():
        pass

    @abstractclassmethod
    def transform_list():
        pass

    @abstractclassmethod
    def transform_dict():
        pass