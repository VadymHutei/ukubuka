class ProductEntity:

    _id = None
    _name = None
    _description = None

    def __init__(self, data):
        self._id = data.get('id')
        self._name = data.get('name')
        self._description = data.get('description')

    def getId(self):
        return self._id

    def getName(self):
        return self._name

    def getDescription(self):
        return self._description

    def toArray(self):
        return {
            'id': self._id,
            'name': self._name,
            'description': self._description,
        }