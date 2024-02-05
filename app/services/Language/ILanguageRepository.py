from abc import ABC

from repositories.IActiveRepository import IActiveRepository
from repositories.ICodeRepository import ICodeRepository
from repositories.IRepository import IRepository


class ILanguageRepository(
    ICodeRepository,
    IActiveRepository,
    IRepository,
    ABC,
):
    pass