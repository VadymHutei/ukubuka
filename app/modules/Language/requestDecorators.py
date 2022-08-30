from functools import wraps

from flask import request, redirect, url_for, g


def languageRedirect(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if 'language' in kwargs:
            if kwargs['language'] not in g.t.languages:
                kwargs['language'] = g.t.default_language.code
                if request.blueprint is None:
                    fName = f.__name__
                else:
                    fName = request.blueprint + '.' + f.__name__
                return redirect(url_for(fName, *args, **kwargs))
            language = kwargs['language']
            del kwargs['language']
        else:
            language = g.t.default_language.code
        request.ctx['language'] = g.t.languages[language]
        return f(*args, **kwargs)
    return decoratedFunction
