from flask import g
from modules.Language.Translator import Translator


def _(text):
    translator = Translator.getInstance()
    return translator.get_translation(text, g.current_language.code)


def view(x):
    if x is None:
        return ''
    if isinstance(x, bool):
        return 'yes' if x else 'no'
    return x


filters = {
    '_': _,
    'view': view,
}
