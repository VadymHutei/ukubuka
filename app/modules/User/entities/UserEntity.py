from vendor.ukubuka.Entity import Entity


class UserEntity(Entity):

    properties = {
        'ID': 'id',
        'email': 'email',
        'firstName': 'first_name',
        'lastName': 'last_name',
        'registeredDatetime': 'registered_datetime',
    }
    booleanProperties = {
        'isBlocked': 'is_blocked',
    }