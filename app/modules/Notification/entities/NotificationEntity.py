from modules.Notification.services.NotificationService import NotificationService


class NotificationEntity:

    def __init__(self, text, type=NotificationService.INFO_TYPE):
        self._text = text
        self._type = type if type in NotificationService.TYPES else NotificationService.INFO_TYPE

    @property
    def text(self):
        return self._text

    @property
    def type_(self):
        return self._type