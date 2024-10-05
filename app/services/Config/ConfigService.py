from entities.Config.ConfigEntity import ConfigEntity
from services.Config.IConfigRepository import IConfigRepository
from services.Service import Service


class ConfigService(Service):

    APP_CONFIG_KEY = 'app_config'

    def __init__(self, repository: IConfigRepository):
        self._repository = repository

    def get_config(self) -> dict[str, ConfigEntity]:
        config_data = self._repository.find_all()

        return {entity.code: entity.value for entity in config_data}