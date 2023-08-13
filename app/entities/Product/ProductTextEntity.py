from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from entities.Language.LanguageEntity import LanguageEntity
from exceptions.ProductException import ProductException


@dataclass
class ProductTextEntity:

    id: int
    product_id: int
    language: Optional[LanguageEntity]
    name: str
    description: str
    created_at: datetime
    updated_at: datetime

    @property
    def language_code(self):
        if self.language:
            return self.language.code
        else:
            return ProductException('Language data is not set')