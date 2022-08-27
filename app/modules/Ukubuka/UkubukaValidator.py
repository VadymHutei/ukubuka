from vendor.ukubuka.validator import Validator


class UkubukaValidator(Validator):

    INT_MIN_VALUE = -2147483648
    INT_MAX_VALUE = 2147483647
    UNSIGNED_INT_MIN_VALUE = 0
    UNSIGNED_INT_MAX_VALUE = 4294967295

    @classmethod
    def DB_int(cls, ID: int, unsigned: bool = True) -> bool:
        if isinstance(ID, int):
            if unsigned:
                return cls.UNSIGNED_INT_MIN_VALUE <= ID <= cls.INT_MAX_VALUE
            else:
                return cls.INT_MIN_VALUE <= ID <= cls.INT_MAX_VALUE
        return False

    @classmethod
    def int_ID(cls, ID: int) -> bool:
        if isinstance(ID, int):
            return cls.DB_int(ID, True)
        return False

    @classmethod
    def text_ID(cls, ID: str) -> bool:
        if isinstance(ID, str):
            try:
                return cls.DB_int(int(ID), True)
            except:
                return False
        return False
