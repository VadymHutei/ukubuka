from typing import Optional


class UserNameEntity:

    def __init__(
        self,
        first_name: Optional[str] = None,
        last_name: Optional[str] = None,
    ):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        name_list = []
        if self.first_name:
            name_list.append(self.first_name)
        if self.last_name:
            name_list.append(self.last_name)
        return ' '.join(name_list) if name_list else ''
