from ukubuka.entity.AbstractEntity import AbstractEntity


class ProductEntity(AbstractEntity):

    _attributesList = (
        'id',
        'name',
        'description',
    )