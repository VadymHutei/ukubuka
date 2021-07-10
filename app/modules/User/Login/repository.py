from config import DB_CREDENTIALS
from vendor.Ukubuka.repository import Repository


class LoginRepository(Repository):

    def __init__(self):
        super().__init__()
        self._setCredentials(DB_CREDENTIALS)