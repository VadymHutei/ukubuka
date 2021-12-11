class UserEntity:

    def __init__(self, data):
        self._ID = data.get('id')
        self._email = data.get('email')
        self._firstName = data.get('first_name')
        self._lastName = data.get('last_name')
        self._isConfirmed = bool(data.get('is_confirmed'))
        self._registeredDatetime = data.get('registered_datetime')

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email

    @property
    def firstName(self):
        return self._firstName

    @firstName.setter
    def firstName(self, firstName):
        self._firstName = firstName

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def isConfirmed(self):
        return self._isConfirmed

    @isConfirmed.setter
    def isConfirmed(self, isConfirmed):
        self._isConfirmed = isConfirmed

    @property
    def registeredDatetime(self):
        return self._registeredDatetime

    @registeredDatetime.setter
    def registeredDatetime(self, registeredDatetime):
        self._registeredDatetime = registeredDatetime