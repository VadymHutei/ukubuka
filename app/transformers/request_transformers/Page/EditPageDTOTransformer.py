from flask import Request

from data_transfer_objects.Page.EditPageDTO import EditPageDTO
from transformers.request_transformers.RequestTransformer import RequestTransformer


class EditPageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> EditPageDTO:
        return EditPageDTO(
            id=int(request.form.get('id')),
            code=request.form.get('code'),
            template=request.form.get('template'),
            layout=request.form.get('layout'),
            is_active=request.form.get('is_active') is not None,
        )