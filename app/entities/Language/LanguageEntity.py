from dataclasses import dataclass

from entities.Entity import Entity
from value_objects.Language.LanguageVO import LanguageVO


@dataclass(kw_only=True)
class LanguageEntity(Entity, LanguageVO):

    id: int