from functools import wraps

from flask import redirect, url_for


class LanguageService:

    def __init__(self, repository):
        self._repository = repository
        self._languages = self._getLanguages()
        self._defaultLanguage = self._getDefaultLanguage()
        self._translates = self._getTranslates()

    def langRedirect(self):
        def decorator(f):
            @wraps(f)
            def decoratedFunction(*args, **kwargs):
                if kwargs['language'] not in self._languages:
                    kwargs['language'] = self._defaultLanguage['code']
                    return redirect(url_for(f.__name__, *args, **kwargs))
                return f(*args, **kwargs)
            return decoratedFunction
        return decorator

    def translate(self, text, language=None):
        if language is None:
            language = self._defaultLanguage['code']
        if language not in self._languages:
            return ''
        print(text)
        print(self._translates[language])
        return self._translates[language].get(text, text)

    def _getLanguages(self):
        languages = self._repository.getLanguages()
        return {language['code']: language for language in languages}

    def _getDefaultLanguage(self):
        return self._repository.getDefaultLanguage()

    def _getTranslates(self):
        translates = {}
        translatesData = self._repository.getTranslates()

        for row in translatesData:
            if row['language'] not in translates:
                translates[row['language']] = {}
            
            translates[row['language']][row['text']] = row['translate']

        return translates