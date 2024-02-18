from abc import ABC

from repositories.IActiveEntityRepository import IActiveEntityRepository
from repositories.IEntityWithCodeRepository import IEntityWithCodeRepository
from repositories.IRepository import IRepository


class ILanguageRepository(
    IEntityWithCodeRepository,
    IActiveEntityRepository,
    IRepository,
    ABC,
):
    pass