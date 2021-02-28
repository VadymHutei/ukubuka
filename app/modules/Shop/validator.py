import re

from ukubuka.validator import Validator


class ShopValidator(Validator):

    def catalogID(catalogID):
        if isinstance(catalogID, str):
            return bool(re.fullmatch(r'[0-9]{1,8}', catalogID))
        return False

    def catalogAlias(catalogAlias):
        if isinstance(catalogAlias, str):
            return bool(re.fullmatch(r'[0-9a-zA-Z_-]{1,64}', catalogAlias))
        return False

    def categoryID(categoryID):
        if isinstance(categoryID, str):
            return bool(re.fullmatch(r'[0-9]{1,8}', categoryID))
        return False

    def categoryAlias(categoryAlias):
        if isinstance(categoryAlias, str):
            return bool(re.fullmatch(r'[0-9a-zA-Z_-]{1,64}', categoryAlias))
        return False

    def productID(productID):
        if isinstance(productID, str):
            return bool(re.fullmatch(r'[0-9]{1,8}', productID))
        return False

    def productAlias(productAlias):
        if isinstance(productAlias, str):
            return bool(re.fullmatch(r'[0-9a-zA-Z_-]{1,64}', productAlias))
        return False

    def SKUID(SKUID):
        if isinstance(SKUID, str):
            return bool(re.fullmatch(r'[0-9]{1,12}', SKUID))
        return False

    def SKUAlias(SKUAlias):
        if isinstance(SKUAlias, str):
            return bool(re.fullmatch(r'[0-9a-zA-Z_-]{1,64}', SKUAlias))
        return False