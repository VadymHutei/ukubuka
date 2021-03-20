from ukubuka.AbstractService import AbstractService


class ACPService(AbstractService):

    def __init__(self, repository):
        self._repository = repository

    def getCategories(self):
        return self._repository.getCategories()