from functools import wraps

from flask import request, current_app

from modules.Language.repository import LanguageRepository
from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.exceptions.LanguageException import LanguageException


class LanguageService:

    def __init__(self):
        self._repository = LanguageRepository()
        self._defaultLanguage = self._getDefaultLanguage()
        self._languages = self._getLanguages()
        self._translations = self._getTranslations()

    @property
    def defaultLanguage(self):
        return self._defaultLanguage

    @property
    def languages(self):
        return self._languages

    @property
    def translations(self):
        return self._translations


    def _getDefaultLanguage(self):
        return LanguageEntity(self._repository.getDefaultLanguage())

    def _getLanguages(self):
        return {row['code']: LanguageEntity(row) for row in self._repository.getLanguages()}

    def _getTranslations(self):
        translations = {}

        for row in self._repository.getTranslations():
            if row['text'] not in translations:
                translations[row['text']] = {}
            translations[row['text']][row['language']] = row['translation']

        return translations


    def inAvailableLanguages(self, code):
        return code in self._languages

    def hasTranslation(self, text):
        return text in self._translations

    def addTranslation(self, text, translations={}):
        if not text:
            return

        for languageCode in self._languages.keys():
            self._repository.addTranslation(text, languageCode, translations.get(languageCode, ''))

    def reloadTranslations(self):
        self._translations = self._getTranslations()

    def translate(self, text, languageCode=None):
        if languageCode is None:
            languageCode = request.ctx['language'].code

        if not self.inAvailableLanguages(languageCode):
            raise LanguageException(f'The site does not support this language: {languageCode}')

        if not self.hasTranslation(text):
            self.addTranslation(text)
            self.reloadTranslations()
            return text

        if self.hasTranslation(text) and self._translations[text][languageCode] == '':
            return text

        return self._translations[text][languageCode]







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
        translates = self._repository.getTranslationsForLanguage(language)
        
        return {row['text']: row['translation'] for row in translates}

    def getAvailableLanguages(self):
        return {code: language for code, language in self.languages.items() if language.isActive}

    def _getTranslationsByLanguage(self):
        translations = {}

        for row in self._repository.getTranslations():
            if row['language'] not in translations:
                translations[row['language']] = {}
            translations[row['language']][row['text']] = row['translation']

        return translations

    def _getTranslations(self):
        translations = {}

        translationsData = self._repository.getTranslations()
        for row in translationsData:
            if row['text'] not in translations:
                translations[row['text']] = {}
            translations[row['text']][row['language']] = row['translation']

        return translations

    @staticmethod
    def getInstance():
        return getattr(current_app, 'languageService', False) or LanguageService()