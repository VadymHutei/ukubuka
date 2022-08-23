from typing import Optional


class UserNameEntity:

    def __init__(
        self,
        firstName: Optional[str] = None,
        lastName: Optional[str] = None,
    ):
        self.firstName = firstName
        self.lastName = lastName

    def __str__(self):
        nameList = []
        if self.firstName:
            nameList.append(self.firstName)
        if self.lastName:
            nameList.append(self.lastName)
        return ' '.join(nameList) if nameList else ''