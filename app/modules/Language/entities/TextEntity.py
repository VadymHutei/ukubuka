class TextEntity:

    def __init__(self, data):
        self._text = data['text']
        self._ID = data.get('id')
        self._translations = {}

    @property
    def text(self):
        return self._text

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def translations(self):
        return self._translations

    @translations.setter
    def translations(self, translations):
        self._translations = translations