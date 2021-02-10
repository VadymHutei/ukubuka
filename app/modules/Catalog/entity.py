from ukubuka.collection import Collection


class CatalogEntity(Collection):

    def __init__(self, products=[]):
        self._items = products