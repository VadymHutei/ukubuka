from transformers.response_transformers.web.WebResponseTransformer import WebResponseTransformer


class WebACPResponseTransformer(WebResponseTransformer):

    ACP_DATE_FORMAT = '%d-%m-%Y %H:%M:%S'