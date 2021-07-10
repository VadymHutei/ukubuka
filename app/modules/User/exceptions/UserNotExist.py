class UserNotExist(Exception):

    def __init__(self, message=None):
        if message is None:
            message = 'user not exist'
        super().__init__(message)