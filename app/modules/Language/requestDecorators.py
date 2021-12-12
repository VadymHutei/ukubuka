from functools import wraps

from flask import request, redirect, url_for

from modules.Language.services.LanguageService import LanguageService


def languageRedirect(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        languageService = LanguageService.getInstance()

        if 'language' in kwargs:
            if kwargs['language'] not in languageService.languages:
                kwargs['language'] = languageService.defaultLanguage.code
                if request.blueprint is None:
                    fName = request.blueprint + '.' + f.__name__
                else:
                    fName = f.__name__
                return redirect(url_for(fName, *args, **kwargs))
            language = kwargs['language']
            del kwargs['language']
        else:
            language = languageService.defaultLanguage.code
        request.ctx['language'] = languageService.languages[language]
        return f(*args, **kwargs)
    return decoratedFunction