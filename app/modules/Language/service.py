from functools import wraps

from flask import redirect, url_for, request

from modules.Language.repository import LanguageRepository


class LanguageService:

    def __init__(self):
        self.repository = LanguageRepository()
        self.defaultLanguage = self.repository.getDefaultLanguage()
        self.languages = {language['code']: language for language in self.repository.getLanguages()}
        self.translations = self._getTranslations()

    def languageRedirect(self):
        def decorator(f):
            @wraps(f)
            def decoratedFunction(*args, **kwargs):
                if 'language' in kwargs:
                    if kwargs['language'] not in self.languages:
                        kwargs['language'] = self.defaultLanguage['code']
                        return redirect(url_for(f.__name__, *args, **kwargs))
                    language = kwargs['language']
                    del kwargs['language']
                else:
                    language = self.defaultLanguage['code']
                request.cnx['language'] = self.languages[language]['code']
                return f(*args, **kwargs)
            return decoratedFunction
        return decorator

    def translate(self, text, language=None):
        if language is None:
            language = self.defaultLanguage['code']
        if language not in self.languages:
            return text
        if language not in self.translations:
            return text
        if text in self.translations[language] and self.translations[language][text] == '':
            return text
        if text not in self.translations[language]:
            for language in self.languages:
                self.repository.addTranslation(language, text, '')
                self.reloadTranslations()

        return self.translations[language].get(text, text)

    def getTranslationsForLanguage(self, language):
        translates = self.repository.getTranslationsForLanguage(language)
        
        return {row['text']: row['translation'] for row in translates}

    def reloadTranslations(self):
        self.translations = self._getTranslations()

    def _getTranslations(self):
        # return {row['language']: {row['text']: row['translation']} for row in self.repository.getTranslations()}
        translates = {}

        for row in self.repository.getTranslations():
            if row['language'] not in translates:
                translates[row['language']] = {}
            
            translates[row['language']][row['text']] = row['translation']

        return translates