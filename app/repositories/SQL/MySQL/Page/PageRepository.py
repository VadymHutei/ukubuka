from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLCodeRepository import MySQLCodeRepository
from repositories.SQL.MySQL.MySQLCodeTextRepository import MySQLCodeTextRepository
from repositories.SQL.MySQL.MySQLTextRepository import MySQLTextRepository
from services.Page.IPageRepository import IPageRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageEntityTransformer import PageEntityTransformer


class PageRepository(
    MySQLCodeTextRepository,
    MySQLTextRepository,
    MySQLCodeRepository,
    IPageRepository,
):

    mapper = PageMapper
    text_mapper = PageTextMapper
    transformer = PageEntityTransformer