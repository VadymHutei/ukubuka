class HTTPTransformerMethods:

    @staticmethod
    def bool_param(param: bool) -> str:
        return 'yes' if param else 'no'