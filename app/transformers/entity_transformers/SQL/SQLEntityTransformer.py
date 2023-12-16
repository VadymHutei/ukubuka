from entities.Entity import Entity
from transformers.entity_transformers.EntityTransformer import EntityTransformer


class SQLEntityTransformer(EntityTransformer):

    @classmethod
    def transform(cls, db_row: dict) -> Entity:
        pass