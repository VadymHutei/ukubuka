class UserAlreadyExist(Exception):
    
    def __init__(self, message=None):
        if message is None:
            message = 'user already exist'
        super().__init__(message)