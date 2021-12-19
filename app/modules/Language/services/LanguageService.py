import re

from flask import request, current_app

from modules.Language.repositories.LanguageRepository import LanguageRepository
from modules.Language.entities.LanguageEntity import LanguageEntity
from modules.Language.entities.TextEntity import TextEntity
from modules.Language.exceptions.LanguageException import LanguageException


class LanguageService:

    def __init__(self):
        self._languageRepository = LanguageRepository()

    def getDefaultLanguage(self):
        defaultLanguageData = self._languageRepository.getDefaultLanguage()

        if defaultLanguageData is None:
            return None

        return LanguageEntity(defaultLanguageData)

    def getLanguages(self):
        languagesData = self._languageRepository.getLanguages()

        return {row['code']: LanguageEntity(row) for row in languagesData}

    def getTexts(self):
        return {row['id']: TextEntity(row) for row in self._languageRepository.getTexts()}

        return None if textData is None else TextEntity(textData)

    def addText(self, textEntity):
        self._languageRepository.addText(textEntity.text)
        if textEntity.translations:
            self.updateTextTranslations(textEntity)

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
    
    def getTranslationsByTextID(self, textID):
        translations = self._languageRepository.getTranslationsByTextID(textID)

        return {row['language']: row['translation'] for row in translations}

    def getTextByID(self, textID):
        textData = self._languageRepository.getTextByID(textID)

        if textData is None:
            return None

        textEntity = TextEntity(textData)
        textEntity.translations = self.getTranslationsByTextID(textID)

        return textEntity

    def deleteTranslations(self, textID):
        self._languageRepository.deleteTranslations(textID)

    def deleteText(self, textID):
        self._languageRepository.deleteText(textID)

    def updateTextTranslations(self, textEntity):
        self._languageRepository.updateTranslations({
            'textID': textEntity.ID,
            'translations': textEntity.translations,
        })