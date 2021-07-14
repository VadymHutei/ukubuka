from functools import wraps

from flask import request, current_app

from modules.Language.repository import LanguageRepository


class LanguageService:

    def __init__(self):
        self.repository = LanguageRepository()
        self.defaultLanguage = self.repository.getDefaultLanguage()
        self.languages = {language['code']: language for language in self.repository.getLanguages()}
        self.translations = self._getTranslations()

    def translate(self, text, language=None):
        if language is None:
            language = request.ctx['language']
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

    def pathWithLanguage(self, path, language):
        pathSegments = path.split('/')
        if not pathSegments:
            return f'/{language}/'
        del pathSegments[0]
        if pathSegments[0] in self.languages:
            pathSegments[0] = language
        else:
            pathSegments.insert(0, language)
        res = '/' + '/'.join(pathSegments)
        print(res)
        return res

    def getTranslationsForLanguage(self, language):
        translates = self.repository.getTranslationsForLanguage(language)
        
        return {row['text']: row['translation'] for row in translates}

    def reloadTranslations(self):
        self.translations = self._getTranslations()

    def getAvailableLanguages(self):
        return {code: language for code, language in self.languages.items() if language.get('is_active', 0) == 1}

    def _getTranslations(self):
        translates = {}

        for row in self.repository.getTranslations():
            if row['language'] not in translates:
                translates[row['language']] = {}
            translates[row['language']][row['text']] = row['translation']

        return translates

    @staticmethod
    def getInstance():
        return getattr(current_app, 'languageService', False) or LanguageService()