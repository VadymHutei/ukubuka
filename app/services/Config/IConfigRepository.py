from abc import ABC

from repositories.Repository import Repository


class IConfigRepository(Repository, ABC):
    pass