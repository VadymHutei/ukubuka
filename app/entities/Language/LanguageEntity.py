from dataclasses import dataclass

from entities.IEntity import IEntity
from value_objects.Language.LanguageVO import LanguageVO


@dataclass(kw_only=True)
class LanguageEntity(IEntity, LanguageVO):

    id: int