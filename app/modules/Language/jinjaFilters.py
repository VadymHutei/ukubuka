from flask import g
from jinja2 import pass_environment
from markupsafe import Markup

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

def checked(value: bool) -> str:
    return 'checked' if value else ''

@pass_environment
def checkbox(env, value: bool) -> str:
    result = '<input type="checkbox"'
    if value:
        result += ' checked'
    result += ' disabled>'

    if env.autoescape:
        result = Markup(result)

    return result

def none(value):
    return '-' if value is None else value


filters = {
    '_': _,
    'view': view,
    'checked': checked,
    'checkbox': checkbox,
    'none': none,
}
