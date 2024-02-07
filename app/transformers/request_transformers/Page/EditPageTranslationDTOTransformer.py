from flask import Request

from data_transfer_objects.Page.EditPageTranslationDTO import EditPageTranslationDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class EditPageTranslationDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> EditPageTranslationDTO:
        return EditPageTranslationDTO(
            language_id=int(request.form.get('language_id')),
            title=request.form.get('title'),
        )