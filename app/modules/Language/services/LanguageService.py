import re

from flask import request, current_app

from modules.Language.repositories.LanguageRepository import LanguageRepository
from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.entities.TextEntity import TextEntity
from modules.Language.exceptions.LanguageException import LanguageException


class LanguageService:

    def __init__(self):
        self._languageRepository = LanguageRepository()
        self._defaultLanguage = self.getDefaultLanguage()
        self._languages = self.getLanguages()
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


    def getDefaultLanguage(self):
        return LanguageEntity(self._languageRepository.getDefaultLanguage())

    def getLanguages(self):
        return {row['code']: LanguageEntity(row) for row in self._languageRepository.getLanguages()}

    def _getTexts(self):
        return [TextEntity(row) for row in self._languageRepository.getTexts()]

    def getTexts(self):
        return {row['id']: TextEntity(row) for row in self._languageRepository.getTexts()}

        return None if textData is None else TextEntity(textData)

    def addText(self, textEntity):
        self._languageRepository.addText(textEntity.text)
        if textEntity.translations:
            self.updateTranslations(textEntity)

    def  _setTranslations(self):
        translations = self.getTranslations()
        for textEntity in self._texts:
            textEntity.translations = translations.get(textEntity.ID, {})

    def getTranslations(self):
        translations = {}

        for row in self._languageRepository.getTranslations():
            if row['text_id'] not in translations:
                translations[row['text_id']] = {}
            translations[row['text_id']][row['language']] = row['translation']

        return translations

    def _saveText(self, textEntity):
        if textEntity.ID is None:
            textID = self._languageRepository.addText(textEntity.text)
            textEntity.ID = textID
        self._languageRepository.setTranslations(textEntity.ID, textEntity.translations)
        self._reloadTexts()
    
    def getTranslationsByTextID(self, textID):
        return {row['language']: row['translation'] for row in self._languageRepository.getTranslationsByTextID(textID)}

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
        translates = self._languageRepository.getTranslationsForLanguage(language)
        
        return {row['text']: row['translation'] for row in translates}

    def getTextByID(self, textID):
        textData = self._languageRepository.getTextByID(textID)

        if textData is None:
            return None

        textEntity = TextEntity(textData)
        textEntity.translations = self.getTranslationsByTextID(textID)

        return textEntity

    def updateTranslations(self, data):
        translations = {}

        pattern = re.compile('translation_(' + '|'.join(self._languages.keys()) + ')')
        for fieldName, fieldValue in data.items():
            result = pattern.search(fieldName)
            if result:
                translations[result.group(1)] = fieldValue

        self._languageRepository.updateTranslations({
            'textID': data['textID'],
            'translations': translations,
        })
        self._setTranslations()

    def deleteTranslations(self, textID):
        self._languageRepository.deleteTranslations(textID)

    def deleteText(self, textID):
        self._languageRepository.deleteText(textID)

    def updateTextTranslations(self, textEntity):
        self._languageRepository.updateTranslations({
            'textID': textEntity.ID,
            'translations': textEntity.translations,
        })

    @staticmethod
    def getInstance():
        return getattr(current_app, 'languageService', False) or LanguageService()