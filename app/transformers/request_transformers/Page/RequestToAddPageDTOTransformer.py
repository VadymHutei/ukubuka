from datetime import datetime

from flask import Request

from transformers.request_transformers.RequestTransformer import RequestTransformer
from value_objects.Page.PageVO import PageVO


class RequestToAddPageDTOTransformer(RequestTransformer):

    @classmethod
    def transform(cls, request: Request) -> PageVO:
        return PageVO(
            code=request.form.get('code'),
            template=request.form.get('template'),
            layout=request.form.get('layout'),
            is_active=request.form.get('is_active') is not None,
            created_at=datetime.now(),
        )