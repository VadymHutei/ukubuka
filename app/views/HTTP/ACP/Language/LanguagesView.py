from re import TEMPLATE
from views.HTTP.View import View


class LanguagesView(View):

    TEMPLATE = 'v1/acp/language/languages.html'

    _title = 'Languages'