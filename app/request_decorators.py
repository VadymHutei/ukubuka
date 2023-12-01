from functools import wraps

from flask import current_app as app, g, redirect, request, url_for

from service_container import sc
from services.Language.LanguageService import LanguageService


def with_language(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        language_service: LanguageService = sc.get(LanguageService)

        if 'language_code' in kwargs:
            if kwargs['language_code'] not in app.config['AVAILABLE_LANGUAGE_CODES']:
                kwargs['language_code'] = g.default_language.code

                endpoint = f.__name__

                if request.blueprint is not None:
                    endpoint = request.blueprint + '.' + endpoint

                return redirect(url_for(endpoint, *args, **kwargs))

            g.current_language = language_service.get_by_code(kwargs['language_code'])
        else:
            g.current_language = g.default_language

        del kwargs['language_code']

        return f(*args, **kwargs)

    return decorated_function