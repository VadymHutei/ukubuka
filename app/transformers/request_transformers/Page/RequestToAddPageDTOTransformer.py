from flask import Request

from data_transfer_objects.Page.AddPageDTO import AddPageDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class RequestToAddPageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> AddPageDTO:
        return AddPageDTO(
            code=request.form.get('code'),
            template=request.form.get('template'),
            layout=request.form.get('layout'),
            is_active=request.form.get('is_active') is not None,
        )