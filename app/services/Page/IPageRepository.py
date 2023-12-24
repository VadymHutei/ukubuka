from repositories.ICodeRepository import ICodeRepository
from repositories.ICodeTextRepository import ICodeTextRepository
from repositories.IRepository import IRepository
from repositories.ITextRepository import ITextRepository


class IPageRepository(
    IRepository,
    ICodeRepository,
    ITextRepository,
    ICodeTextRepository
):
    pass