from flask import Request

from data_transfer_objects.Language.EditLanguageDTO import EditLanguageDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class EditLanguageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> EditLanguageDTO:
        return EditLanguageDTO(
            code=request.form.get('code'),
            name=request.form.get('name'),
            is_active=request.form.get('is_active') is not None,
        )