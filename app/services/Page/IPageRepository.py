from abc import ABC

from repositories.IActiveRepository import IActiveRepository
from repositories.ICodeRepository import ICodeRepository
from repositories.ICodeTextRepository import ICodeTextRepository
from repositories.IRepository import IRepository
from repositories.ITextRepository import ITextRepository


class IPageRepository(
    ICodeTextRepository,
    ITextRepository,
    ICodeRepository,
    IActiveRepository,
    IRepository,
    ABC,
):
    pass