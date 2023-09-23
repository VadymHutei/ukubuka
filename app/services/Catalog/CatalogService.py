from services.Catalog.ICatalogRepository import ICatalogRepository
from services.Service import IService


class CatalogService(IService):

    def __init__(self, repository: ICatalogRepository) -> None:
        self.repository: ICatalogRepository = repository