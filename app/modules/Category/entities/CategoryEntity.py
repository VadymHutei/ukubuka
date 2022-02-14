class CategoryEntity():

    def __init__(self, data):
        self._ID = data['id']
        self._alias = data['alias']
        self._parentID = data['parent_id']
        self._name = data['name']
        self._createdDatetime = data['created_datetime']
        self._changedDatetime = data['changed_datetime']
        self._isActive = bool(data['is_active'])

    @property
    def ID(self):
        return self._ID

    @ID.setter
    def ID(self, ID):
        self._ID = ID

    @property
    def alias(self):
        return self._alias

    @alias.setter
    def alias(self, alias):
        self._alias = alias

    @property
    def parentID(self):
        return self._parentID

    @parentID.setter
    def parentID(self, parentID):
        self._parentID = parentID

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def createdDatetime(self):
        return self._createdDatetime

    @createdDatetime.setter
    def createdDatetime(self, createdDatetime):
        self._createdDatetime = createdDatetime

    @property
    def changedDatetime(self):
        return self._changedDatetime

    @changedDatetime.setter
    def changedDatetime(self, changedDatetime):
        self._changedDatetime = changedDatetime

    @property
    def isActive(self):
        return self._isActive

    @isActive.setter
    def isActive(self, isActive):
        self._isActive = isActive