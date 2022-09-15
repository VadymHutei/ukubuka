from flask import g
from modules.Language.Translator import Translator


def _(text):
    translator = Translator.getInstance()
    return translator.get_translation(text, g.current_language.code)


def pathWithLanguage(path, language):
    pathSegments = path.split('/')

    if not pathSegments:
        return f'/{language}/'

    translator = Translator.getInstance()
    del pathSegments[0]

    if pathSegments[0] in translator.languages:
        pathSegments[0] = language
    else:
        pathSegments.insert(0, language)

    return '/' + '/'.join(pathSegments)


def view(x):
    if x is None:
        return ''
    if isinstance(x, bool):
        return 'yes' if x else 'no'
    return x


filters = {
    '_': _,
    'pathWithLanguage': pathWithLanguage,
    'view': view,
}
