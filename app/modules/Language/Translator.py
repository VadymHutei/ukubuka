from flask import request

from modules.Language.entities.TextEntity import TextEntity
from modules.Language.exceptions.LanguageException import LanguageException
from modules.Language.services.LanguageService import LanguageService


class Translator:

    _instance = None

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = Translator()
        return cls._instance

    def __init__(self):
        self._languageService = LanguageService()

        self._defaultLanguage = self._languageService.getDefaultLanguage()
        self._languages = self._languageService.getLanguages()
        self._setTexts()

    @property
    def defaultLanguage(self):
        return self._defaultLanguage

    @property
    def languages(self):
        return self._languages

    @property
    def availableLanguages(self):
        return {languageCode: language for languageCode, language in self._languages.items() if language.isActive}

    def translate(self, text, language=None):
        if language is None:
            if hasattr(request, 'ctx'):
                language = request.ctx['language'].code
            else:
                return text

        if language not in self._languages:
            raise LanguageException(f'The site does not support this language: {language}')

        textID = self._getTextIDByText(text)

        if (textID is None):
            textEntity = TextEntity({'text': text})
            self._languageService.addText(textEntity)
            self._setTexts()
            return text

        translation = self._texts[textID].translations.get(language)

        if translation is None:
            textTranslations = {}
            for languageCode in self._languages:
                textTranslations[languageCode] = ''
            self._texts[textID].translations = textTranslations
            self._languageService.updateTextTranslations(self._texts[textID])
            return text
        
        return translation if translation else text

    def _setTexts(self):
        self._texts = self._languageService.getTexts()
        self._textIDs = {text.text: text.ID for text in self._texts.values()}
        self._setTranslations()

    def _setTranslations(self):
        translations = self._languageService.getTranslations()

        for textID in self._texts:
            if textID not in translations:
                textTranslations = {}
                for languageCode in self._languages:
                    textTranslations[languageCode] = ''
                self._texts[textID].translations = textTranslations
                self._languageService.updateTextTranslations(self._texts[textID])
            else:
                self._texts[textID].translations = translations[textID]

    def _getTextIDByText(self, text):
        for textEntity in self._texts.values():
            if text == textEntity.text:
                return textEntity.ID
        return None