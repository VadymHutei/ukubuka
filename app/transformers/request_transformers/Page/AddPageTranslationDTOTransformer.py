from flask import Request

from data_transfer_objects.Page.AddPageTranslationDTO import AddPageTranslationDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class AddPageTranslationDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> AddPageTranslationDTO:
        return AddPageTranslationDTO(
            language_id=int(request.form.get('language_id')),
            title=request.form.get('title'),
        )