from entity_mappers.SQL.MySQL.Page.PageMapper import PageMapper
from entity_mappers.SQL.MySQL.Page.PageTextMapper import PageTextMapper
from repositories.SQL.MySQL.ActiveRepository import ActiveRepository
from repositories.SQL.MySQL.CodeTextRepository import CodeTextRepository
from services.Page.IPageRepository import IPageRepository
from transformers.entity_transformers.SQL.MySQL.Page.PageEntityTransformer import PageEntityTransformer
from transformers.entity_transformers.SQL.MySQL.Page.PageTextEntityTransformer import PageTextEntityTransformer


class PageRepository(CodeTextRepository, ActiveRepository, IPageRepository):

    mapper = PageMapper
    text_mapper = PageTextMapper
    transformer = PageEntityTransformer
    translation_transformer = PageTextEntityTransformer