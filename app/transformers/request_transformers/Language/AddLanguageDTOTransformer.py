from flask import Request

from data_transfer_objects.Language.AddLanguageDTO import AddLanguageDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class AddLanguageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> AddLanguageDTO:
        return AddLanguageDTO(
            code=request.form.get('code'),
            name=request.form.get('name'),
            is_active=request.form.get('is_active') is not None,
        )