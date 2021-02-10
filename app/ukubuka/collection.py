class Collection:

    _items = []

    def __init__(self, items=[]):
        self._items = items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)