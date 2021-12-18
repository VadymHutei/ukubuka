from functools import wraps
import re

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
            textEntity.ID = textID
        self._repository.setTranslations(textEntity.ID, textEntity.translations)
        self._reloadTexts()
    
    def _getTranslationsByTextID(self, textID):
        return {row['language']: row['translation'] for row in self._repository.getTranslationsByTextID(textID)}

    def _reloadTexts(self):
        self._texts = self._getTexts()
        self._setTranslations()

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

    def getTextByID(self, textID):
        textData = self._repository.getTextByID(textID)
        textEntity = TextEntity(textData)
        textEntity.translations = self._getTranslationsByTextID(textID)

        return textEntity

    def updateTranslations(self, data):
        translations = {}

        pattern = re.compile('translation_(' + '|'.join(self._languages.keys()) + ')')
        for fieldName, fieldValue in data.items():
            result = pattern.search(fieldName)
            if result:
                translations[result.group(1)] = fieldValue

        self._repository.updateTranslations({
            'textID': data['textID'],
            'translations': translations,
        })
        self._setTranslations()

    def deleteTranslations(self, textID):
        self._repository.deleteTranslations(textID)
        self._setTranslations()

    def deleteText(self, textID):
        self._repository.deleteText(textID)
        self._reloadTexts()

    @staticmethod
    def getInstance():
        return getattr(current_app, 'languageService', False) or LanguageService()