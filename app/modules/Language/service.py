from functools import wraps

from flask import request, current_app

from modules.Language.repository import LanguageRepository
from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.entities.TextEntity import TextEntity
from modules.Language.exceptions.LanguageException import LanguageException


class LanguageService:

    def __init__(self):
        self._repository = LanguageRepository()
        self._defaultLanguage = self._getDefaultLanguage()
        self._languages = self._getLanguages()
        self._texts = self._getTexts()
        self._setTranslations()

    @property
    def defaultLanguage(self):
        return self._defaultLanguage

    @property
    def languages(self):
        return self._languages

    @property
    def texts(self):
        return self._texts


    def _getDefaultLanguage(self):
        return LanguageEntity(self._repository.getDefaultLanguage())

    def _getLanguages(self):
        return {row['code']: LanguageEntity(row) for row in self._repository.getLanguages()}

    def _getTexts(self):
        return [TextEntity(row) for row in self._repository.getTexts()]

    def _setTranslations(self):
        translations = self._getTranslations()
        for textEntity in self._texts:
            textEntity.translations = {row['language']: row['translation'] for row in translations.get(textEntity.ID, [])}

    def _getTranslations(self):
        translations = {}

        for row in self._repository.getTranslations():
            if row['text_id'] not in translations:
                translations[row['text_id']] = []
            translations[row['text_id']].append(row)

        return translations

    def _saveText(self, textEntity):
        if textEntity.ID is None:
            textID = self._repository.addText(textEntity.text)
            print(type(textID))
            textEntity.ID = textID
        self._repository.setTranslations(textEntity.ID, textEntity.translations)


    def translate(self, text, language=None):
        if language is None:
            language = request.ctx['language'].code

        if language not in self._languages:
            raise LanguageException(f'The site does not support this language: {language}')

        for textEntity in self._texts:
            if text == textEntity.text:
                if language not in textEntity.translations:
                    textEntity.translations[language] = ''
                    self._saveText(textEntity)
                    return text
                return textEntity.translations[language] if textEntity.translations[language] else text
        self._saveText(TextEntity({'text': text}))
        return text

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

    @staticmethod
    def getInstance():
        return getattr(current_app, 'languageService', False) or LanguageService()