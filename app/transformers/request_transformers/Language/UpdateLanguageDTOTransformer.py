from flask import Request

from data_transfer_objects.Language.UpdateLanguageDTO import UpdateLanguageDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class UpdateLanguageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> UpdateLanguageDTO:
        return UpdateLanguageDTO(
            id=int(request.form.get('id')),
            code=request.form.get('code'),
            name=request.form.get('name'),
            is_active=request.form.get('is_active') is not None,
        )