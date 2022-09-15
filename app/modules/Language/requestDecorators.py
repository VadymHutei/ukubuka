from functools import wraps

from flask import g, redirect, request, url_for


def languageRedirect(f):
    @wraps(f)
    def decoratedFunction(*args, **kwargs):
        if 'language' in kwargs:
            if kwargs['language'] not in g.t.available_languages:
                kwargs['language'] = g.t.default_language.code
                if request.blueprint is None:
                    f_name = f.__name__
                else:
                    f_name = request.blueprint + '.' + f.__name__
                return redirect(url_for(f_name, *args, **kwargs))
            g.current_language = g.t.languages[kwargs['language']]
            del kwargs['language']
        else:
            g.current_language = g.t.default_language
        return f(*args, **kwargs)
    return decoratedFunction
