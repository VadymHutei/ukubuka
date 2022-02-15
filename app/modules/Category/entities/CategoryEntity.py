from vendor.ukubuka.Entity import Entity


class CategoryEntity(Entity):

    properties = {
        'ID': 'id',
        'alias': 'alias',
        'parentID': 'parent_id',
        'name': 'name',
        'createdDatetime': 'created_datetime',
        'changedDatetime': 'changed_datetime',
    }
    booleanProperties = {
        'isActive': 'is_active',
    }