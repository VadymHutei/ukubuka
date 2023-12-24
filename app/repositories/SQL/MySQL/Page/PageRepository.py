from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.MySQLCodeTextRepository import MySQLCodeTextRepository
from services.Page.IPageRepository import IPageRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageEntityTransformer import PageEntityTransformer
from transformers.entity_transformers.SQL.MySQL.Page.PageTranslationEntityTransformer import \
    PageTranslationEntityTransformer


class PageRepository(MySQLCodeTextRepository, IPageRepository):

    mapper = PageMapper
    text_mapper = PageTextMapper
    transformer = PageEntityTransformer
    translation_transformer = PageTranslationEntityTransformer