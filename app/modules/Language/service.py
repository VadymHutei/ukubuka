from functools import wraps

from flask import request, current_app

from modules.Language.repository import LanguageRepository
from modules.Language.entities.LanguageEntity import LanguageEntity


class LanguageService:

    def __init__(self):
        self.repository = LanguageRepository()
        self.defaultLanguage = self.repository.getDefaultLanguage()
        self.languages = {language['code']: language for language in self.repository.getLanguages()}
        self.translations = self._getTranslationsByLanguage()
        self._translations = self._getTranslations()
        self._languages = self._getLanguages()

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

    def getTranslations(self):
        return self._translations

    def getLanguages(self):
        return self._languages

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
        return res

    def getTranslationsForLanguage(self, language):
        translates = self.repository.getTranslationsForLanguage(language)
        
        return {row['text']: row['translation'] for row in translates}

    def reloadTranslations(self):
        self.translations = self._getTranslationsByLanguage()

    def getAvailableLanguages(self):
        return {code: language for code, language in self.languages.items() if language.get('is_active', 0) == 1}

    def _getTranslationsByLanguage(self):
        translations = {}

        for row in self.repository.getTranslations():
            if row['language'] not in translations:
                translations[row['language']] = {}
            translations[row['language']][row['text']] = row['translation']

        return translations

    def _getTranslations(self):
        translations = {}

        translationsData = self.repository.getTranslations()
        for row in translationsData:
            if row['text'] not in translations:
                translations[row['text']] = {}
            translations[row['text']][row['language']] = row['translation']

        return translations

    def _getLanguages(self):
        return [LanguageEntity(row) for row in self.repository.getLanguages()]

    @staticmethod
    def getInstance():
        return getattr(current_app, 'languageService', False) or LanguageService()