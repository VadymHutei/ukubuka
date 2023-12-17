from flask import Request

from data_transfer_objects.Page.UpdatePageTranslationDTO import UpdatePageTranslationDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class RequestToUpdatePageTranslationDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> UpdatePageTranslationDTO:
        return UpdatePageTranslationDTO(
            id=int(request.form.get('id')),
            title=request.form.get('title'),
        )