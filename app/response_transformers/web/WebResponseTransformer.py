from response_transformers.ResponseTransformer import ResponseTransformer


class WebResponseTransformer(ResponseTransformer):

    @staticmethod
    def checkbox(value: bool) -> str:
        checked = 'checked' if value else ''
        return f'<input type="checkbox" {checked}>'