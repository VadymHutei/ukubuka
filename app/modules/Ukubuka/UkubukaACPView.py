from modules.Notification.entities.NotificationEntity import NotificationEntity
from modules.Notification.services.NotificationService import NotificationService
from modules.Ukubuka.UkubukaView import UkubukaView


class UkubukaACPView(UkubukaView):

    def __init__(self, template=None):
        super().__init__(template)

        self._notifications = []

    @property
    def notifications(self):
        return self._notifications

    def _prepareTemplateData(self):
        super()._prepareTemplateData()

        self._templateData['notifications'] = self._notifications
    
    def info(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.INFO_TYPE))
    
    def warning(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.WARNING_TYPE))
    
    def success(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.SUCCESS_TYPE))
    
    def error(self, text):
        self._notifications.append(NotificationEntity(text, NotificationService.ERROR_TYPE))
