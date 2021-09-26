class LanguageEntity:

    def __init__(self, data):
        self._code = data['code']
        self._name = data['name']
        self._isActive = data['is_active']
        self._isDefault = data['is_default']

    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name

    @property
    def isActive(self):
        return self._isActive

    @property
    def isDefault(self):
        return self._isDefault