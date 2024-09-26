from abc import ABC

from transformers.entity_transformers.SQL.SQLEntityTransformer import SQLEntityTransformer


class MySQLEntityTransformer(SQLEntityTransformer, ABC):
    pass
