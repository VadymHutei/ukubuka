from typing import Callable


class ValidationRule:

    def __init__(self, callback: Callable, message: str):
        self.callback = callback
        self.error_message = message
