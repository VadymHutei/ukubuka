from dataclasses import dataclass


@dataclass
class UserNameEntity:

    first_name: str|None = None
    last_name: str|None = None

    def __str__(self):
        name_list = []
        if self.first_name:
            name_list.append(self.first_name)
        if self.last_name:
            name_list.append(self.last_name)

        return ' '.join(name_list) if name_list else ''