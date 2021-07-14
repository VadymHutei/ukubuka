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

    def getTranslationsForLanguage(self, language):
        translates = self.repository.getTranslationsForLanguage(language)
        
        return {row['text']: row['translation'] for row in translates}

    def reloadTranslations(self):
        self.translations = self._getTranslations()

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