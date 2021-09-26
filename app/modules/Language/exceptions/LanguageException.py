class LanguageException(Exception):

    def __init__(self, message=None):
        if message is None:
            message = 'Language exception'
        super().__init__(message)