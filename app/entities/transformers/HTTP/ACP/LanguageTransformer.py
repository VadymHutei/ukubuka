from typing import Any
from entities.transformers.AbstractTransformer import AbstractTransformer

from entities.transformers.HTTP.HTTPTransformerMethods import HTTPTransformerMethods
from entities.LanguageEntity import LanguageEntity


class LanguageTransformer(AbstractTransformer, HTTPTransformerMethods):

    @classmethod
    def transform(cls, language: LanguageEntity) -> dict:
        return {
            'code': language.code,
            'name': language.name,
            'is_active': cls.bool_param(language.is_active),
            'is_default': cls.bool_param(language.is_default),
        }

    @classmethod
    def transform_list(cls, languages: list[LanguageEntity]) -> list:
        return [cls.transform(language) for language in languages]

    @classmethod
    def transform_dict(cls, languages: dict[Any, LanguageEntity]) -> dict:
        return {key: cls.transform(language) for key, language in languages.items()}