from entities.Config.ConfigEntity import ConfigEntity
from services.Service import Service
from services.Config.ConfigRepositoryInterface import ConfigRepositoryInterface


class ConfigService(Service):

    APP_CONFIG_KEY = 'app_config'

    def __init__(self, repository: ConfigRepositoryInterface):
        self._repository = repository

    def get_config(self) -> dict[str, ConfigEntity]:
        config_data = self._repository.get_config()

        return {entity.code: entity for entity in config_data}