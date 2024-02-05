from entity_mappers.SQL.MySQL.Language.LanguageMapper import LanguageMapper
from repositories.SQL.MySQL.ActiveRepository import ActiveRepository
from repositories.SQL.MySQL.CodeRepository import CodeRepository
from services.Language.ILanguageRepository import ILanguageRepository
from transformers.entity_transformers.SQL.MySQL.Language.LanguageEntityTransformer import LanguageEntityTransformer


class LanguageRepository(CodeRepository, ActiveRepository, ILanguageRepository):

    mapper = LanguageMapper
    transformer = LanguageEntityTransformer