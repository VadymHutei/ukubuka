from vendor.ukubuka.validator import Validator


class UkubukaValidator(Validator):
    
    @staticmethod
    def intID(ID, unsigned=True):
        min = 0 if unsigned else -2147483648
        max = 4294967295 if unsigned else 2147483647
        if isinstance(ID, int):
            return min <= ID <= max
        return False