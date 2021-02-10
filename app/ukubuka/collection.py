class Collection:

    _items = []

    def addItem(self, item):
        self._items.append(item)

    def getItems(self):
        return self._items

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)