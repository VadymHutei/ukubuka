from modules.Base.views.View import View
from modules.Notification.entities.NotificationEntity import NotificationEntity
from modules.Notification.services.NotificationService import NotificationService


class ACPView(View):

    def __init__(self):
        super().__init__()

        self._notifications = []

    @property
    def notifications(self):
        return self._notifications

    def _prepare_template_data(self):
        super()._prepare_template_data()

        self.template_data['notifications'] = self._notifications

    def info(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.INFO_TYPE))

    def warning(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.WARNING_TYPE))

    def success(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.SUCCESS_TYPE))

    def error(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.ERROR_TYPE))
