from abc import ABC


class AbstractEntity(ABC):

    _attributesList = ()
    _attributes = {}

    def __init__(self, data):
        for name, value in data.items():
            if name in self._attributesList:
                self._attributes[name] = value

    def __getitem__(self, key):
        return self._attributes.get(key, None)

    def toArray(self):
        return self._attributes