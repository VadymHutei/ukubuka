from functools import wraps

from flask import redirect, url_for

from modules.Language.repository.LanguageRepository import LanguageRepository


languageRepository = LanguageRepository()
languages = {row['code']: row for row in languageRepository.getLanguages()}
defaultLanguage = languageRepository.getDefaultLanguage()

def langRedirect(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if kwargs['language'] not in languages:
            kwargs['language'] = defaultLanguage['code']
            return redirect(url_for(f.__name__, *args, **kwargs))
        return f(*args, **kwargs)
    return decoratedFunction