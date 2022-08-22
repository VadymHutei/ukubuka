class UserEntity():

    def __init__(self, ID=None):
        self._ID = ID

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID