from flask import Request

from data_transfer_objects.Page.UpdatePageDTO import UpdatePageDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class RequestToUpdatePageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> UpdatePageDTO:
        return UpdatePageDTO(
            id=int(request.form.get('id')),
            code=request.form.get('code'),
            template=request.form.get('template'),
            layout=request.form.get('layout'),
            is_active=request.form.get('is_active') is not None,
        )